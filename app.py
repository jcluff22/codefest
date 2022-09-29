#!/usr/bin/env python3

from flask import Flask, request, send_from_directory
from database_update import main_update, db_connect, get_collection, add_document, main_update
import json

app = Flask(__name__, static_url_path='web/static')

db_name = "ife-charity-mongodb"

@app.route("/")
def home():
    return app.send_static_file('form.html')

@app.route("/school", methods=['POST'])
def school():
    data = request.form['input_form']
    main_update(data, db_name, "school")
    

@app.route("/child", methods=['POST'])
def child():
    data = request.form['input_form']
    main_update(data, db_name, "child")
    

@app.route("/sponsor", methods=['POST'])
def sponsor():
    data = request.form['input_form']
    main_update(data, db_name, "sponsor")
    