# Team BeanBois
# Joan Chirinos
# SoftDev2 pd08
# K07 -- Import/Export Bank
# 2019-03-01

# Pokédex
# https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
# To import, I open a connection to the server. I check if the db 'test'
# exists. Then, I open the db and open the collection. If the db didn't exist,
# I upload BeanBois.json into the collection 'pokemon', which creates the db
# and the collection. Otherwise, I just continue on with my DB stuff.
#
# This assumes that if the db 'test' exists, the collection 'pokemon' and the
# uploaded documents MUST exist

# import only the things we'll use?
from pymongo import MongoClient
# import json to parse JSON
import json


# connect to a mongo server
# adress should be string, port should be int
# default port = 27017
def connect(address, port=27017):
    client = MongoClient(address, port)
    return client


# get a database given a client and a db name
def getDatabase(client, name):
    # We could do this ONLY if name is a valid Python attribute name.
    # We can't guarantee it, so we use the dictionary-style syntax instead
    # db = client.name
    db = client[name]
    return db


# get a collection given the database and the collection name
def getCollection(db, name):
    # We could do this ONLY if name is a valid Python attribute name.
    # We can't guarantee it, so we use the dictionary-style syntax instead
    # collection = db.name
    collection = db[name]
    return collection


# inserts a document into a collection
# returns the document ID
# assumes the document is a list of dictionaries structured like JSON
# assumes the document either has no ID (one will be created) OR a UNIQUE ID
def insertDocuments(collection, documents):
    id = collection.insert_many(documents)
    return id


# gets documents in collection which match the querydict (Python dictionary)
# returns an iterable of all documents found
def findDocuments(collection, queryDict={}, fields={}):
    docs = collection.find(queryDict, fields)
    return docs


# counts all documents, or all documents that match queryDict, in a collection
def countDocuments(collection, queryDict={}):
    return collection.count_documents(queryDict)

# TESTING METHOD #
def test():
    # connecting to my droplet (using the default port)
    client = connect('206.189.236.112')

    dbnames = client.list_database_names()
    pokemon_exists = 'test' in dbnames
    # get db
    db = getDatabase(client, 'test')

    # get collection
    collection = getCollection(db, 'pokemon')

    # insert document if db not exists
    if not pokemon_exists:
        docs = []
        with open('BeanBois.json', 'r') as f:
            raw_json = f.read()
            docs = json.loads(raw_json)
            docs = docs['pokemon']

        print(insertDocuments(collection, docs))

    # query that finds pokemon with
    # weaknesses == Fire
    query = {"weaknesses": "Fire"}
    # fields return the name
    fields = {'_id': 0, 'name': 1}
    pokemonWeakToFire = findDocuments(collection, query, fields)
    print('Pokemon weak to fire:')
    for i in pokemonWeakToFire:
        print(i['name'])

    # query that finds pokemon with
    # spawn_chance < 0.1
    # AND
    #   type == Grass
    #   OR
    #   type == Fire
    query = {"spawn_chance": {'$lt': 0.1}, '$or': [{"type": "Grass"}, {"type": "Fire"}]}
    # fields return the name and the type(s)
    fields = {'_id': 0, 'name': 1, 'type': 1}
    rarePokemonEitherFireOrGrass = findDocuments(collection, query, fields)
    print('Rare pokemon that are either Fire or Grass type:')
    for i in rarePokemonEitherFireOrGrass:
        print('{} -- {}'.format(i['name'], ' and '.join(i['type'])))

    query = {"type": "Fire", 'type': 'poison'}
    # fields return the name
    fields = {'_id': 0, 'name': 1, 'type': 1}
    pokemonWeakToFire = findDocuments(collection, query, fields)
    print('Pokemon weak to beans:')
    for i in pokemonWeakToFire:
        print('{} -- {}'.format(i['name'], i['type']))

# test()











# beans
