from pymongo import MongoClient

MONGO_DB_HOST = 'mongo'
MONGO_DB_PORT = '27017'
DB_NAME = 'house-finder'

client = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db=DB_NAME):
    return client[db]
