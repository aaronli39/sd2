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
3) run mongod on your droplet ($mongod -v --bind_ip_all --noauth --dbpath db3/) <--- specific for AK
4) we then insert the reformatted json docs into the collection
'''

import pymongo
import json

#SERVER_ADDR = "69.55.59.139" #Aaron
SERVER_ADDR = "178.128.156.17" #AK
client = pymongo.MongoClient(SERVER_ADDR)
db = client.aaronoza
col = db.history #hw


#importation mechanism since our file was reformatted
with open('history.json') as f:
    lines = f.readlines()
    for line in lines:
        data = json.loads(line)
        #print(line)
        col.insert(data)


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
    #[print(i, "\n") for i in cursor]
    lst=[]
    for i in cursor:
        lst.append(i)
    print(lst)
    return lst

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
    lst=[]
    for i in cursor:
        lst.append(i["event"]["description"])
    print(lst)
    #[print(i["event"]["description"], "\n") for i in cursor]
    print("----- End of Descriptions found for date:", date, "-----\n")
    return lst # list of relevant entries

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
        #[print(i["event"]["description"], "\n") for i in cursor]
        lst=[]
        for i in cursor:
            lst.append(i["event"]["description"])
        print(lst)
        return lst
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
        lst=[]
        for i in cursor:
            if phrase in i["event"]["description"]:
                print("Date:", i["event"]["date"], "\n", i["event"]["description"], "\n")
                lst.append(i["event"]["description"])
        return lst
    else:
        print("Please input another phrase to search! \n")

# test
yearAll(100)
# yearDesc(100)
# placeDesc("Americas")
find("Alexander")
