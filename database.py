from pymongo import MongoClient
Client=MongoClient("mongodb://localhost:27017")
mydatabase=Client.event
mycollection=mydatabase.collection1
Cursor=mycollection.find()
for i in Cursor:
    print(i)