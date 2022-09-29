import getpass
import json
import pymongo


def db_connect(client, db_name):
    db = client[db_name]
    return db    


def get_collection(db, input_collection):
    collection = db[input_collection]
    return collection


def add_document(collection, input_data):
    document_id = collection.insert_one(input_data).inserted_id
    print("Inserted document with _id {}".format(document_id))
    return document_id

def main_update(inputjson, db_name, collection_name):
    """Connect to the API for MongoDB, create DB and collection, perform CRUD operations"""
    client = pymongo.MongoClient(CONNECTION_STRING)
    try:
        client.server_info() # validate connection string
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError("Invalid API for MongoDB connection string or timed out when attempting to connect")

    db = db_connect(client, db_name)
    collection = get_collection(db, collection_name)
    document_id = add_document(collection, inputjson)
    return document_id
