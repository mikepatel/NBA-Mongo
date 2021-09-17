"""


"""
################################################################################
# Imports
import pandas as pd
import pymongo

# import from other modules in /app/
import config


################################################################################
def get_data(player_name):
    # connect to MongoDB instance
    client = pymongo.MongoClient(config.URL)

    # navigate to db, collection
    db = client["nba"]
    collection = db["players"]

    # query
    fields_to_exclude = [
        "_id",
        "Unnamed: 0",
        "player_height",
        "player_weight",
        "college",
        "country",
        "draft_round",
        "draft_number",
        "net_rating",
        "oreb_pct",
        "dreb_pct",
        "ast_pct"
    ]
    fields_to_exclude = {field: 0 for field in fields_to_exclude}

    query = {
        #"draft_year": {
        #    "$gte": "2015",
        #    "$lte": "2019"
        #}
        "player_name": player_name
    }
    results = collection.find(query, fields_to_exclude)
    results = list(results)

    # convert to dataframe
    df = pd.DataFrame(results)

    # close connection
    client.close()

    return df
