# Aaron Li
# SoftDev2 pd8
# K07 -- Import/Export Bank
# 2019-02-29

# We used the English history dataset (found here http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en).
# The set is a collection of historical events. Each entry has an associated date, description, location, and associated literature.
# The collection was imported using the mongoimport command on our droplets.

# IMPORT INSTRUCTIONS:
# http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en
# 1) Click and download the link above to download the dataset, name it whatever you want with a .json file type.
# 2) run $ python3 findrep.py <name_of_ur_file>.json to convert the file into a valid json format
# 3) run mongod on your droplet ($mongod -v --bind_ip_all --noauth --dbpath db3/) <--- specific for AK
# 4) we then insert the reformatted json docs into the collection

import pymongo
import json

SERVER_ADDR = "69.55.59.139" #Aaron
client = pymongo.MongoClient(SERVER_ADDR)
db = client.history
col = db.files

# connect to address
def connect(addr):
    client = pymongo.MongoClient(addr)
    return client

# import function(only need to do this once)
def imp(db, col):
    if "files" in db.list_collection_names(): return
    print("Importing history data...")
    #importation mechanism since our file was reformatted
    with open('history.json') as f:
        lines = f.readlines()
        temp = []  
        for line in lines:
            try:
                data = json.loads(line)
                temp.append(data)
            except:
                print("Something unexpected happened.")
                break
        col.insert_many(temp)
        print("Import successful.")

# Given a year, return historical entries found given input:
# an integer year (eg: 900)
# a string date in yyyy/mm/dd format (eg: 2001/01/17)
def yearAll(year, col):
    if type(year) != type(12) and type(year) != type(""):
        print("Please enter a valid date.\n")
        return

    cursor = col.find({"event.date": str(year)})
    if cursor.count() == 0:
        print("Sorry, this year wasn't found.\n")
        return
    lst = []
    [print(i, "\n") for i in cursor]
    for i in cursor:
        lst.append(i)
    return lst


# Given a specific date, return relevant historical entry
def yearDesc(date, col):
    if type(date) != type(12) and type(date) != type(""):
        print("Please enter a valid date.")
        return [-1, "Please enter a valid date."]

    cursor = col.find({"event.date": str(date)})
    if cursor.count() == 0:
        print("Sorry, this year wasn't found.")
        return [-1, "Sorry, this year wasn't found."]

    # print("\n----- Descriptions found for date:", date, "-----\n")
    lst = []
    # [print(i["event"]["description"], "\n") for i in cursor]
    # print("----- End of Descriptions found for date:", date, "-----\n")

    for i in cursor:
        lst.append(i["event"]["description"])
    return lst  # list of relevant entries


# Given a place or topic (category 2) returns relevant historical entry descriptions
# first letter of place should be capitalized
# (eg: Americas, Asia, Religion, Arts and Sciences)
def placeDesc(place):
    if type(place) == type("abc"):
        cursor = col.find({"event.category2": place})
        # [print(i["event"]["description"], "\n") for i in cursor]
        lst = []
        for i in cursor:
            lst.append(i["event"]["description"])
        print(lst)
        return lst
    else:
        print("Please input a valid place.\n")


# Given a word (or phrase), returns entries containing the word (or phrase)
# and the date
def find(phrase, col):
    if type(phrase) == type("abc"):
        cursor = col.find({"event.lang": "en"})
        lst = []
        try:
            for i in cursor:
                if phrase in i["event"]["description"]:
                    # print(
                    #     "Date:", i["event"]["date"], "\n", i["event"]["description"], "\n"
                    # )
                    lst.append(i["event"]["description"])
            return lst
        except:
            return -1
    else:
        print("Please input another phrase to search! \n")
        return -1

# test
# yearAll("2012/12/31")
# yearDesc("2012/12/31")
# placeDesc("Americas")
# find("T")
