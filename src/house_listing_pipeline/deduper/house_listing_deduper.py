from bs4 import BeautifulSoup
import hashlib
import json
import os
import re
import requests
import sys
import pickle
import redis
import lxml

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'common'))

import mongodb_client

from cloudAMQP_client import CloudAMQPClient

HOUSE_LISTING_TABLE_NAME = "house-listings"

config_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "config", "config.json")
with open(config_path) as config_file:
    json_config = json.load(config_file)

db_config = json_config["db"]
queue_config = json_config["rabbit_mq"]

SLEEP_TIME_IN_SECONDS = 1

DEDUP_TASK_QUEUE_URL = queue_config["DEDUP_TASK_QUEUE_URL"]
DEDUP_TASK_QUEUE_NAME = queue_config["DEDUP_TASK_QUEUE_NAME"]

NOTIFICATION_TASK_QUEUE_URL = "amqp://lmmocuap:DPdNdw03IT0laCvkNm66BzP_0iSY3GHk@elephant.rmq.cloudamqp.com/lmmocuap"
NOTIFICATION_TASK_QUEUE_NAME = "notification_task_queue"

dedup_queue_client = CloudAMQPClient(DEDUP_TASK_QUEUE_URL, DEDUP_TASK_QUEUE_NAME)
notification_queue_client = CloudAMQPClient(DEDUP_TASK_QUEUE_URL, DEDUP_TASK_QUEUE_NAME)  

REDIS_HOST = db_config["REDIS_HOST"]
REDIS_PORT = db_config["REDIS_PORT"]

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)

def send_to_redis(task):
    task_id = task["client_id"] + "_new"
    print task_id
    if redis_client.get(task_id) is not None:
        new_list = pickle.loads(redis_client.get(task_id))
        new_list[task["id"]] = task
	print "add new"
        redis_client.set(task_id, pickle.dumps(new_list))
    else:
        new_list = {}
	print "careate new"
        new_list[task['id']] = task
        redis_client.set(task_id, pickle.dumps(new_list))


def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        return

    task = msg

    url = msg['url']

    raw_data = requests.get(url)
    raw_text = raw_data.text
    soup = BeautifulSoup(raw_text, "lxml")

    data = soup.find_all('script', text = re.compile(ur'imgList'))[0].string

    pattern = re.compile('<!--\nvar imgList = (.*?);\n-->')

    m = pattern.match(data)

    stocks = json.loads(m.groups()[0])

    shortIds = ""

    for s in stocks:
        shortIds += s["shortid"]

    img_id_hash = hashlib.md5(shortIds).digest().encode('base64')

    db = mongodb_client.get_db()

    same_img_listings = list(db[HOUSE_LISTING_TABLE_NAME].find({'img_id_hash': img_id_hash}))

    if same_img_listings is not None and len(same_img_listings) > 0:
        print 'Duplicated house listing. Ignore'
        return

    task['img_id_hash'] = img_id_hash

    db[HOUSE_LISTING_TABLE_NAME].replace_one({'img_id_hash': task['img_id_hash']}, task, upsert=True)
    print "********************************************* before send to redis"

    gallery = soup.find("div", {"class": "gallery"})
    img_url = ""
    if gallery:
        img = gallery.find("img")
        if img and img.attrs.get("src"):
            img_url = img.attrs.get("src").strip()
    task["img_url"] = img_url
    print img_url
    send_to_redis(task)
    
    #notification_queue_client.sendMessage(task)
    return task
    

def dedup():
    while True:
        if dedup_queue_client is not None:
            msg = dedup_queue_client.getMessage()
            if msg is not None:
                try:
                    handle_message(msg)
                except Exception as e:
                    print e
                    pass
            else:
                break
            dedup_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
        else:
            break
