import datetime
from pymongo import MongoClient
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('../config.ini')

    cluster = MongoClient('mongodb+srv://' + config['MongoDB']['key'])
    db = cluster['houses_data']
    for doc in db['houses_coll_test'].find():
        date_sold = doc['date_sold']
        db.houses_coll.update_one(
            {
                'address_street': doc['address_street'],
                'address_city': doc['address_city'],
                'date_sold': date_sold,
            },
            {'$set': doc},
            upsert=True,
        )



# def main():
#     config = configparser.ConfigParser()
#     config.read('../config.ini')
#
#     cluster = MongoClient('mongodb+srv://' + config['MongoDB']['key'])
#     db = cluster['houses_data']
#
#     # pipeline = [{"$match": {}}, {"$out": "destination_collection"},
#     # ]
#     # db.source_collection.aggregate(pipeline)
#
#     # db['houses_coll'].find().forEach(lambda x: db.getSiblingDB('houses_data')['houses_coll_test'].insert(x))
#     count = 0
#     for doc in db['houses_coll'].find():
#         count += 1
#         date_sold = doc['date_sold']
#         doc['date_sold'] = datetime.datetime.fromtimestamp(doc['date_sold'])
#         doc['creation_date'] = datetime.datetime.fromtimestamp(doc['creation_date'])
#
#         # print(doc)
#         db.houses_coll_test.update_one(
#             {
#                 'address_street': doc['address_street'],
#                 'address_city': doc['address_city'],
#                 'date_sold': date_sold,
#             },
#             {'$set': doc},
#             upsert=True,
#         )
#     print(count)


if __name__ == '__main__':
    main()
