from flask import Flask, Blueprint, render_template
from pymongo import MongoClient
import json
from config.config import DB_PASSWORD

DB_ACCESS = f"mongodb+srv://jsare527:{DB_PASSWORD}@termproject.8hcqb9v.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(DB_ACCESS)
db = client.get_database("MainWebsite")
readings = db.get_collection("readings")


api = Blueprint('api', __name__, template_folder='templates', static_folder='static')

@api.route('/data')
def allData():
    cursor = readings.find({}).sort('$natural', -1)
    arr = []
    for cur in cursor:
        cur.pop('_id')
        arr.append(cur)
    return json.dumps(arr)
