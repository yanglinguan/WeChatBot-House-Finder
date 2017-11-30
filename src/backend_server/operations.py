import json
import os
import pickle
import redis
import sys

from bson.json_util import dumps
from datetime import datetime

#sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

request_id_counter = 0

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)

def submitRequestForm(request_form):
    print request_form
    global request_id_counter
    request_form["request_id"] = str(request_id_counter)
    request_id_counter += 1
    request_form["active"] = True
    
    if redis_client.get(request_form["user_id"]) is not None:
        print "update request for client..."
        request_table = pickle.loads(redis_client.get(request_form["user_id"]))
        request_table[request_form["request_id"]] = request_form
        redis_client.set(request_form["user_id"], pickle.dumps(request_table))
    else:
        print "add new client request..."
        redis_client.rpush("client_list", request_form['user_id'])
        request_table = {}
        request_table[request_form["request_id"]] = request_form
        redis_client.set(request_form["user_id"], pickle.dumps(request_table))

    result = { "success": True,
                "message": "successfully submit the request",
                "request_id": request_form["request_id"]
            }
    return result

def deleteRequestForm(user_id, request_id):
    if redis_client.get(user_id) is not None:
        print "Delete user request form..."
        request_table = pickle.loads(redis_client.get(user_id))
        request_table[request_id]["active"] = False
        redis_client.set(user_id, pickle.dumps(request_table))
    
    result = { "success": True,
                "message": "successdull delete request",
                "request_id": request_id
                }

        
    return result

def getRequestHistory(user_id):
    if redis_client.get(user_id) is not None:
        print "Get Request History..."
        request_table = pickle.loads(redis_client.get(user_id))
        
        return request_table
    else:
        return {}

def getRequestDetail(user_id, request_id):
    if redis_client.get(user_id) is not None:
        print "Get Request Detail..."
        request_table = pickle.loads(redis_client.get(user_id))
        
        return request_table[request_id]
    else:
        return {}
