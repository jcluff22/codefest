import getpass
import json
import pymongo

db_name = 'ife-charity-mongodb'
CONNECTION_STRING = 'mongodb://ife-charity-mdb:gyTxoa3F2HoN6Iwb2mhOwpjkTVl4wa6HrzDODrdNHYT8HAQCIybrIUM7gdN6LWgDpLkAAGmh1auuaTZpXG2RnQ==@ife-charity-mdb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@ife-charity-mdb@' 
collection_name = 'test1'

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

def main():
    """Connect to the API for MongoDB, create DB and collection, perform CRUD operations"""
    client = pymongo.MongoClient(CONNECTION_STRING)
    try:
        client.server_info() # validate connection string
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError("Invalid API for MongoDB connection string or timed out when attempting to connect")

    inputjson = {"test":"test1","test2":"test2"}
    db = db_connect(client, db_name)
    collection = get_collection(db, collection_name)
    document_id = add_document(collection, inputjson)

    # collection = create_database_unsharded_collection(client)
    # document_id = insert_sample_document(collection)

if __name__ == "__main__":
    main()