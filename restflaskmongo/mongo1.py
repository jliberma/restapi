#!/usr/bin/env python

from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')

mydb = client['test-database-1']


myrecord = {
        "author": "Duke",
        "title": "PyMongo 101",
        "tags": ["MongoDB", "PyMongo", "Tutorial"],
        "date": datetime.datetime.utcnow()
        }

record_id = mydb.mytable.insert(myrecord)

print(record_id)
print(mydb.collection_names())
