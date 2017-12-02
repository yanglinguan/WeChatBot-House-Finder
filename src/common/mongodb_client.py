from pymongo import MongoClient
import json
import os

config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config", "config.json")
with open(config_path) as config_file:
    json_config = json.load(config_file)

config = json_config["db"]

MONGO_DB_HOST = config["MONGO_HOST"]
MONGO_DB_PORT = config["MONGO_PORT"]
DB_NAME = 'house-finder'

client = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db=DB_NAME):
    return client[db]
