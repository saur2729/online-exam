from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # Connect to mongodb

dbs = client.list_database_names()
print(dbs)

for db in dbs:
  if db == "job-scheduler":
    print(db, " => ", client[db].list_collection_names(), "\n")
    my_col = client[db].list_collection_names()[0]
    x = client[db][my_col].find_one()
    print(x["_id"])

