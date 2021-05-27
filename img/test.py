import pymongo
from pymongo import MongoClient
username = 'appUser'
password = 'passwordForAppUser'

client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

mydb = client["app_db"]
known = mydb["nimbleevents"]

list_to_process = []

myquery = { "u_process" : 'no' }
records = known.find(myquery)
for r in records:
    list_to_process.append(r)

print(list_to_process)
