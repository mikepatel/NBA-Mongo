"""
Michael Patel
June 2021

Project description:
    A data science project using NBA stats data and MongoDB

File description:
    Test file to populate/query a players' database

"""
################################################################################
# Imports
import pymongo

import config  # credentials


################################################################################
# ----- DB SETUP ----- #
# first, create a client object and connect
url = "mongodb+srv://" + config.username + ":" + config.password + "@cluster0.34mdn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)

# Database --> Collection (Table) --> Document (Record)
# db
db = client["nba"]
#print(client.list_database_names())

# collection (table)
col = db["players"]
#print(db.list_collection_names())


# ----- INSERT ----- #
"""
x = {
    "name": "Michael",
    "team": "Mavs"
}
"""

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

# ----- SUMMARY ----- #
print(f'Databases: {client.list_database_names()}')
print(f'Collections: {db.list_collection_names()}')
print(f'Documents in collection: {col.name}:')
for result in col.find({}, {"_id": 0}):
    print(result)

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
print()
print("Teams that contain the substring 'er' in their names:")
query = {"team": {"$regex": ".*er.*"}}
for result in col.find(query, {"_id": 0}):  # exclude "_id" field in results
    print(result)
