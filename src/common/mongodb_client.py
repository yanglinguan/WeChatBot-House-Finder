from pymongo import MongoClient
import json

config = json.load(open('../config/db.config.json'))

MONGO_DB_HOST = config["MONGO_HOST"]
MONGO_DB_PORT = config["MONGO_PORT"]
DB_NAME = 'house-finder'

client = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db=DB_NAME):
    return client[db]
