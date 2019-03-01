# Aaron Li, Jack Lu: LuLians
# SoftDev2 pd8
# K06 -- Yummy Mongo Py
# 2019-02-28

import pymongo

SERVER_ADDR = "69.55.59.139"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.hw
col = db.rests
curs = col.find({"borough": "Queens"})

# restaurants with specified borough
def printBorough(boro):
    if type(boro) == type("asdf"):
        cursor = col.find(
            {
                "borough": boro
            }
        )
        [print(x) for x in cursor]
    else:
        print("Please enter a string borough\n")

# restaurants with specified zipcode
def printZip(zipcode):
    if type(zipcode) == type(1):
        cursor = col.find(
            {
                "address.zipcode": str(zipcode)
            }
        )
        [print(x) for x in cursor]
    else:
        print("Please enter a valid zipcode\n")

# prints restaurants in zipcode with specified grade
def printZipGrade(zipcode, grade):
    if type(grade) == type("asdf") and type(zipcode) == type(1):
        cursor = col.find(
            {
                "address.zipcode": str(zipcode),
                "grades.grade": grade
            }
        )
        [print(x) for x in cursor]
    else:
        print("Invalid borough or zipcode\n")

# prints restaurants in zipcode with score of < inputs
def printZipScore(zipcode, score):
    if type(score) == type(zipcode) == type(1):
        cursor = col.find(
            {
                "address.zipcode": str(zipcode),
                "grades.score": {"$lt": score}
            }
        )
        [print(x) for x in cursor]
    else:
        print("Invalid Input\n")

# prints percent of restaurants in zipcode with score below threshold
def printPercentBelow(zipcode, score):
    if type(score) == type(zipcode) == type(1):
        total = col.count(
            {
                "address.zipcode": str(zipcode)
            }
        )
        num = col.count(
            {
                "address.zipcode": str(zipcode),
                "grades.score": {"$lt": score}
            }
        )
        print((num / total) * 100.0)
    else:
        print("Invalid Input\n")

# printBorough("Queens")
# printZip(11223)
# printZipGrade(11223, "A")
# printZipScore(11223, 5)
# printPercentBelow(11223, 10)
