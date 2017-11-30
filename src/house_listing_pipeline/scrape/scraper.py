import datetime
import hashlib
import pickle
import redis
import os
import sys
import time

from craigslist import CraigslistHousing

sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SLEEP_TIME_IN_SECONDS = 10

HOUSE_LISTING_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

FILTER_TASK_QUEUE_URL = "amqp://ymcsvgqv:ulM5Xwupq5lJdQ3L0HBy_-xO74CRtGh7@mosquito.rmq.cloudamqp.com/ymcsvgqv"
FILTER_TASK_QUEUE_NAME = "filter_task_queue"

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
cloudAMQP_client = CloudAMQPClient(FILTER_TASK_QUEUE_URL, FILTER_TASK_QUEUE_NAME)


def scrape(city, area, category, filters, clientId, requestId):
    print "city: " + city
    print "area: " + area
    print "category: " + category

    cl_h = CraigslistHousing(site=city, area=area, category=category, filters=filters)

    results = []
    gen = cl_h.get_results(sort_by='newest', geotagged=True, limit=50)

    num_of_new_listings = 0

    while True:
        try:
            result = next(gen)
        except StopIteration:
            break
        except Exception:
            continue

        listing = redis_client.get(result['id'])

        lat = 0
        lon = 0

        if listing is None:
            if result['where'] is None:
                continue

            if result['geotag'] is not None:
                lat = result["geotag"][0]
                lon = result["geotag"][1]
            else:
                continue

            redis_client.set(result['id'], "True")
            redis_client.expire(result['id'], HOUSE_LISTING_TIME_OUT_IN_SECONDS)


            price = 0
            try:
                price = float(result["price"].replace("$", ""))
            except Exception:
                pass

            house_listing = {
                    "url": result["url"],
                    "post_date": result["datetime"],
                    "lat": lat,
                    "lon": lon,
                    "name": result["name"],
                    "price": price,
                    "location": result["where"],
                    "area": result["area"],
                    "client_id": clientId,
                    "request_id": requestId,
		    "id": result["id"],
                    }
            num_of_new_listings = num_of_new_listings + 1
            results.append(house_listing)
            cloudAMQP_client.sendMessage(house_listing)
    print "Fetched %d house listings." % num_of_new_listings
    return results

def do_scrape():

    client_list = redis_client.lrange("client_list", 0, -1)

    for client_id in client_list:
        client_request_table = pickle.loads(redis_client.get(client_id))

        for request_id in client_request_table:
            client_request = client_request_table[request_id]
            if not client_request["active"]:
                continue
            city = client_request["city"]
            area_list = client_request["areas"]
            #category_list = client_request["category"]
            category_list = ["apa"]
            filters = {
                    "min_bedrooms": client_request["min_bedroom"],
                    "max_bedrooms": client_request["max_bedroom"],
                    "min_price": client_request["min_price"],
                    "max_price": client_request["max_price"],
                    "private_bath": client_request["private_bath"],
		    "has_image": True
		    }

        
            all_results = []
            for area in area_list:
                for category in category_list:
                    all_results += scrape(city, area, category, filters, client_id, request_id)

            print("{}: Got {} results for client {}".format(time.ctime(), len(all_results), client_id))

            cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)



#while True:
 #   do_scrape()
  #  cloudAMQP_client.sleep(SLEEP_TIME_BETWEEN_LOOP_IN_SECONDS)

