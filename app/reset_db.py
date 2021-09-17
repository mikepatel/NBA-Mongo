"""


"""
################################################################################
# Imports
import pandas as pd
import pymongo

# import from other modules in /app/
import config


################################################################################
# Main
if __name__ == "__main__":
    # connect to MongoDB instance
    client = pymongo.MongoClient(config.URL)

    # navigate to db, collection
    db = client["nba"]
    collection = db["players"]

    # remove documents from collection
    collection.delete_many({})

    # read in from csv
    df = pd.read_csv(config.CSV_FILEPATH)

    # insert data as documents into collection
    collection.insert_many(df.to_dict("records"))
