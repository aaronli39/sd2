import json
import pymongo

with open("data/prize.json","r") as data:
	data = data.read()
	pyDict = json.loads(data)
	# pyDict has one key-value pair:
	# { "prizes": array of json data with info about Nobel Prizes}
	prizes = pyDict["prizes"]

# print(prizes)

connection,db,col = 0,0,0

def launchDB(addr):
	'''Drop json data on a running server.'''
	global connection, db, col, prizes
	try:
		# remove existing db if there is one
		connection.drop_database(db)
	except:
		pass
	# connect to new given server
	connection = pymongo.MongoClient(addr)
	db = connection.prizes
	col = db.nobel
	# insert array of json data as docs into collection
	col.insert_many(prizes)

def getData(arg, type):
	if (type == "year"):
		results = col.find({"year": arg})
	elif (type == "category"):
		results = col.find({"category": arg})
	data = []
	for result in results:
		data.append(result)
	return data

