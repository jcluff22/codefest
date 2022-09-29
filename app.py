#!/usr/bin/env python3

from flask import Flask, request
from database_update import main_update
import json

app = Flask(__name__)

db_name = "ife-charity-mongodb"

@app.route("/")
def home():
    return "Hello"

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
    main_update(data, db_name, "child")
    