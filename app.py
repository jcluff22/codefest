#!/usr/bin/env python3

from flask import Flask, request, render_template
from database_update import db_connect, get_collection, add_document
from werkzeug.datastructures import ImmutableMultiDict
import json
import pymongo

app = Flask(__name__, static_url_path='')

db_name = "ife-charity-mongodb"
CONNECTION_STRING = 'xxx'
@app.route("/")
def home():
    return render_template('child_registration.html')

@app.route("/school", methods=['POST'])
def school():
    data = request.form.to_dict(flat=False)
    documentid = main_update(data, db_name, "school")
    return render_template('success.html')

@app.route("/child", methods=['POST'])
def child():
    data = request.form.to_dict(flat=False)
    documentid = main_update(data, db_name, "child")
    return render_template('success.html')

@app.route("/sponsor", methods=['POST'])
def sponsor():
    data = request.form.to_dict(flat=False)
    documentid = main_update(data, db_name, "sponsor")
    return render_template('success.html')

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