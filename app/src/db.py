"""
Michael Patel
June 2021

Project description:

File description:

"""
################################################################################
# Imports
import pymongo

import config


################################################################################
# ----- CREATE a DB ----- #
# first, create a client object
url = "mongodb+srv://" + config.username + ":" + config.password + "@cluster0.8mrm9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client["nba_base"]  # name of db: nba_base
print(client.list_database_names())

col = db["players"]  # name of collection (table): players
print(db.list_collection_names())

x = {
    "name": "Michael",
    "team": "Mavs"
}

y = col.insert_one(x)  # name of document (record): x

print("\n\n\n\n")
print(client.list_database_names())
print(db.list_collection_names())
