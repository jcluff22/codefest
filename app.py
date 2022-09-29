#!/usr/bin/env python3

from flask import Flask, request, render_template
from database_update import main_update, db_connect, get_collection, add_document, main_update
import json

app = Flask(__name__, static_url_path='')

db_name = "ife-charity-mongodb"

@app.route("/")
def home():
    return render_template('form.html')

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
    