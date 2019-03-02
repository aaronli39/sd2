# Aaron Li, Aleksandra Koroza: Aaronoza
# SoftDev2 pd8
# K07 -- Import/Export Bank
# 2019-02-29

import pymongo

SERVER_ADDR = "69.55.59.139"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.aaronoza
col = db.history

def yearDesc(date):
    if type(date) == type(123):
        cursor = col.find(
            {
                "result.event.date":
            }
        )