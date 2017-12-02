import wechatpy.utils
from wechatpy import create_reply
from wechatpy.exceptions import (
        InvalidSignatureException, 
        InvalidAppIdException,
)
import pickle
import redis
import os
import json

wechat_config = json.load(open(os.path.join(os.environ["HOUSE_FINDER_HOME"], "config/wechat.config.json")))

TOKEN = wechat_config['TOKEN']
AES_KEY = wechat_config['AESKEY']
APPID = wechat_config['APPID']

db_config = json.load(open(os.path.join(os.environ["HOUSE_FINDER_HOME"], "config/db.config.json")))
REDIS_HOST = db_config["REDIS_HOST"]
REDIS_PORT = db_config["REDIS_PORT"]

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)


def check_signature(request):
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    encrypt_type = request.args.get('encrypt_type', 'raw')
    msg_signature = request.args.get('msg_signature', '')
    wechatpy.utils.check_signature(TOKEN, signature, timestamp, nonce)

def event_handler(msg):
    if msg.event == 'subscribe':
        articles = [{
            'title': 'Submit Request',
            'description': 'submit request to find rent',
            'url': 'http://house.yanglinguan.me/requestForm/userId/' + msg.source,
            },]
        reply = create_reply(articles, msg)
       # reply = create_reply('Welcome to CozyPlaces, Click http://g to submit your request', msg)
        return reply.render()
    return ''
    
def text_handler(msg):
    if "new" in msg.content.lower():
        house_listing = getNewHouse(msg.source)
        if len(house_listing) == 0:
            reply = create_reply("no more new house", msg)
            return reply.render()
        articles = []
        for h in house_listing:
            a = {
                'title': h["name"],
                'description': h["location"],
                'url': h["url"],
                }
            articles.append(a)
        reply = create_reply(articles, msg)
        return reply.render()

    else:
        reply = create_reply(msg.content, msg)
        return reply.render()

def getNewHouse(client_id):
    search_id = client_id + "_new"
    print search_id
    if redis_client.get(search_id) is not None:
        listing = pickle.loads(redis_client.get(search_id))
        l = []
        count = 0
        for i in listing:
            if count < 5:
                l.append(listing[i]);
            else:
                break;
            count += 1;

        for i in l: 
            listing.pop(i['id'])
	    print i['id']
	
        if len(listing) > 0:
            redis_client.set(search_id, pickle.dumps(listing))
        else:
            redis_client.delete(search_id)
        return l
    else:
        return []
        

    

