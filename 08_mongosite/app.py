# Team Team
# Joan Chirinos, Aaron Li, Joyce Liao

import os

from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages
import pprint

from util import pokemon as pk

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/pokemon')
def pokemonLanding():
    return render_template('pokemonLanding.html')

@app.route('/getPokemen', methods=["POST"])
def getMen():

    # connect to DB
    client = pk.connect('206.189.236.112')
    db = pk.getDatabase(client, 'test')
    collection = pk.getCollection(db, 'pokemon')

    types = request.form.getlist('type')
    id = request.form.get('id')
    weaknesses = request.form.getlist('weak')
    all = request.form.get('all')

    query = {}
    if all:
        qtypes = [{'type': i} for i in types]
        qweaknesses = [{'weaknesses': i} for i in weaknesses]
        query = {'$and': qtypes + qweaknesses}
        if id.strip() != '':
            query['id'] = int(id)
        fields = {'_id': 0, 'name': 1, 'weaknesses': 1, 'type': 1, 'img': 1, 'id': 1}
        print('QUERY:')
        pprint.pprint(query)
        print('FIELDS')
        pprint.pprint(fields)
        pokemon = pk.findDocuments(collection, query, fields)
        hasmon = False
        print('OUT')
        pokelist = []
        for i in pokemon:
            pokelist.append(i)
            hasmon = True
        print(pokelist)
        return render_template('pokemonGet.html', hasmon=hasmon, pokemon=pokelist, types=', '.join(types), weaknessess=', '.join(weaknesses), id=id)
    else:
        qtypes = [{'type': i} for i in types]
        qweaknesses = [{'weaknesses': i} for i in weaknesses]
        if qtypes == []:
            qtypes = [{}]
        if qweaknesses == []:
            qweaknesses = [{}]
        query = {'$and': [{'$or': qtypes}, {'$or': qweaknesses}]}
        if id.strip() != '':
            query['id'] = int(id)
        fields = {'_id': 0, 'name': 1, 'weaknesses': 1, 'type': 1, 'img': 1, 'id': 1}
        print('QUERY:')
        pprint.pprint(query)
        print('FIELDS')
        pprint.pprint(fields)
        pokemon = pk.findDocuments(collection, query, fields)
        print('OUT')
        pokelist = []
        hasmon = False
        for i in pokemon:
            pokelist.append(i)
            hasmon = True
        print(pokelist)
        return render_template('pokemonGet.html', hasmon=hasmon, pokemon=pokelist, types=', '.join(types), weaknesses=', '.join(weaknesses), id=id)


if __name__ == '__main__':
    app.debug = True
    app.run()
