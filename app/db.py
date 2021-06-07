"""
Michael Patel
June 2021

Project description:

File description:

"""
################################################################################
# Imports
import pymongo

import config  # credentials


################################################################################
# ----- CREATE a DB ----- #
# first, create a client object
url = "mongodb+srv://" + config.username + ":" + config.password + "@cluster0.8mrm9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client["nba_base"]  # name of db: nba_base
#print(client.list_database_names())

col = db["players"]  # name of collection (table): players
#print(db.list_collection_names())


# ----- INSERT ----- #
x = {
    "name": "Michael",
    "team": "Mavs"
}

#y = col.insert_one(x)  # document (record): x

#print("\n\n\n\n")
#print(client.list_database_names())
#print(db.list_collection_names())

# insert several documents (records)
a = [
    {"name": "LeBron", "team": "Lakers"},
    {"name": "Giannis", "team": "Bucks"},
    {"name": "Kawhi", "team": "Clippers"},
    {"name": "KD", "team": "Nets"},
    {"name": "Luka", "team": "Mavs"},
    {"name": "CP3", "team": "Suns"},
]

#b = col.insert_many(a)
#print("\n\n\n\n")
#print(client.list_database_names())
#print(db.list_collection_names())


# ----- FIND ---- #
"""
for result in col.find():
    print(result)
"""

"""
for result in col.find({"team": "Mavs"}, {"_id": 0}):  # exclude "_id" field in results
    print(result)
"""

# ----- REGEX QUERY ----- #
query = {"team": {"$regex": ".*er.*"}}
for result in col.find(query, {"_id": 0}):
    print(result)
