#!/usr/bin/python3

# Aaron Li, Aleksandra Koroza: Aaronoza
# SoftDev2 pd8
# K07 -- Import/Export Bank
# 2019-02-29

'''
We used the English history dataset (found here https://github.com/jdorfman/awesome-json-datasets). The
set is a collection of historical events. Each entry has an associated date, description, location, and associated literature.
The collection was imported using the mongoimport command on our droplets.
'''

import pymongo

SERVER_ADDR = "69.55.59.139"
# SERVER_ADDR = "178.128.156.17"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.aaronoza
col = db.history

# Given a year, return relevant historical entries
def yearDesc(year):
    if type(year) == type(123):
        cursor = col.find({"result.event.date": str(year)})
        for entry in cursor:
            print(entry)

    else:
        print("Please input a valid year!\n")

# Given a specific date, return relevant historical entry
def dateDesc(date):
    if type(date) == type("abc"):
        cursor = col.find({"result.event.date": str(year)})
        for entry in cursor:
            print(entry)

    else:
        print("Please input a date with the format mm/dd/year \n")

# Given a place (category 2) returns relevant historical entries
def placeDesc(place):
    if type(place) == type("abc"):
        cursor = col.find({"result.event.category2": place})
        for entry in cursor:
            print(entry)

    else:
        print("Please input a valid place! \n")

# Return all entries in a given year and place
def yearPlaceDesc(year,place):
    if type(year) == type(123) and type(place)== type("abc"):
        cursor = col.find({
        "$and":[
        {"result.event.date":str(year)},
        {"result.event.category2":place},
        ]
        })
        for entry in cursor:
            print(entry)

    else:
        print("Please input a valid year and place! \n")


#Given a word (or phrase), returns entries containing the word (or phrase).
def phraseFind(phrase):
    if type(phrase)== type("abc"):
        col.create_index([("description", pymongo.TEXT )]) #text searching https://docs.mongodb.com/manual/text-search/
        cursor = col.find({
        "$text":
        {"$search": phrase}
        }
        )
        for entry in cursor:
            print(entry)

    else:
        print("Please input another phrase to search! \n")
'''
testing
'''

#yearDesc(-292)
#dateDesc()
#placeDesc()
#yearPlaceDesc(-300,"Seleucid Empire")
phraseFind("Napoleonic")