#!/usr/bin/python3

# Aaron Li, Aleksandra Koroza: Aaronoza
# SoftDev2 pd8
# K07 -- Import/Export Bank
# 2019-02-29

'''
We used the English history dataset (found here http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en). 
The set is a collection of historical events. Each entry has an associated date, description, location, and associated literature.
The collection was imported using the mongoimport command on our droplets.
'''

'''
IMPORT INSTRUCTIONS:

http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en

1) Click and download the link above to download the dataset, name it whatever you want with a .json file type.
2) run $ python3 findrep.py <name_of_ur_file>.json to convert the file into a valid json format
'''

import pymongo

SERVER_ADDR = "69.55.59.139"
# SERVER_ADDR = "178.128.156.17"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.aaronoza
col = db.hw

# Given a year, return historical entries found given input:
# an integer year (eg: 900)
# a string date in yyyy/mm/dd format (eg: 2001/01/17)
def yearAll(year):
    cursor = col.find(
        {
            "event.date": str(year)
        }
    )
    if cursor.count() == 0:
        print("Sorry, this year wasn't found.\n")
        return
    [print(i, "\n") for i in cursor]

# Given a specific date, return relevant historical entry
def yearDesc(date):
    if type(date) != type(12) or type(date) != type(""):
        print("Please enter a valid date.\n")
        return

    cursor = col.find(
        {
            "event.date": str(date)
        }
    )
    if cursor.count() == 0:
        print("Sorry, this year wasn't found.")
        return
    print("\n----- Descriptions found for date:", date, "-----\n")
    [print(i["event"]["description"], "\n") for i in cursor]
    print("----- End of Descriptions found for date:", date, "-----\n")

# Given a place or topic (category 2) returns relevant historical entry descriptions
# first letter of place should be capitalized
# (eg: Americas, Asia, Religion, Arts and Sciences)
def placeDesc(place):
    if type(place) == type("abc"):
        cursor = col.find(
            {
                "event.category2": place
            }
        )
        [print(i["event"]["description"], "\n") for i in cursor]
    else:
        print("Please input a valid place.\n")

# Given a word (or phrase), returns entries containing the word (or phrase)
# and the date
def find(phrase):
    if type(phrase) == type("abc"):
        cursor = col.find(
            {
                "event.lang": "en"
            }
        )
        for i in cursor:
            if phrase in i["event"]["description"]:
                print("Date:", i["event"]["date"], "\n", i["event"]["description"], "\n")
    else:
        print("Please input another phrase to search! \n")

# test
yearAll(100)
yearDesc(100)
placeDesc("Americas")
find("valid")
