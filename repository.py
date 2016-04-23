from pymongo import MongoClient
from datetime import datetime

class Repository:
    def __init__(self):
        client = MongoClient("mongodb://localhost:27017")
        self.db = client.twitter

    def save(self, tweet):
        return self.db.tweets.insert_one(tweet)

    def save_many(self, tweets):
        return self.db.tweets.insert_many(tweets)

    def get_coordinates(self):
        return list(self.db.tweets.find({'coordinates': True},{'sevilla': 1, 'betis': 1, 'feria': 1, 'Lat': 1, 'Lng': 1, '_id': 0}))

    def get_totals_by_key(self):
        pass


# r = Repository()
#
# tweets = r.get_coordinates()
#
# for tweet in tweets:
#     print(tweet)

