"""


"""
################################################################################
# Imports
import pandas as pd
import pymongo

# import from other modules in /app/
import config


################################################################################
def query_database():
    # connect to MongoDB instance
    client = pymongo.MongoClient(config.URL)

    # navigate to db, collection
    db = client["nba"]
    collection = db["players"]

    # query
    query = {
        "draft_year": "2015"
    }
    results = collection.find(query, {"_id": 0})  # exclude "_id" field in results
    results = list(results)

    # convert to dataframe
    df = pd.DataFrame(results)
    print(df)
