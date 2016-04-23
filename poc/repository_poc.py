from pymongo import MongoClient
from datetime import datetime


def get_db():
    # client = MongoClient('localhost:27017')
    client = MongoClient("mongodb://localhost:27017")
    db = client.poc
    return db


def add_restaurant(db):
    return db.restaurant.insert_one(
        {
            "address": {
                "street": "2 Avenue",
                "zipcode": "10075",
                "building": "1480",
                "coord": [-73.9557413, 40.7720266]
            },
            "borough": "Manhattan",
            "cuisine": "Mexican",
            "grades": [
                {
                    "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                    "grade": "A",
                    "score": 11
                },
                {
                    "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                    "grade": "B",
                    "score": 17
                }
            ],
            "name": "La chinche pinche",
            "restaurant_id": "41704622"
        }
    )


def get_restaurant(db):
    return db.restaurant.find_one()


db = get_db()

cursor = db.restaurant.find({"cuisine": "Mexican"})

for document in cursor:
    print(document)

# result = add_restaurant(db)
# print(get_restaurant(db))
# ds = db.restaurant
