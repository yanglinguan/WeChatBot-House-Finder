from pymongo import MongoClient
import json
import os
config = json.load(open(os.path.join(os.environ["HOUSE_FINDER_HOME"], "config/db.config.json")))

MONGO_DB_HOST = config["MONGO_HOST"]
MONGO_DB_PORT = config["MONGO_PORT"]
DB_NAME = 'house-finder'

client = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db=DB_NAME):
    return client[db]
