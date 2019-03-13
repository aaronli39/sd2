# Team Mongo-Lians
# Joan Chirinos, Aaron Li, Joyce Liao

import os

from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages
import pprint

from util import pokemon as pk
from util import history as hist
from util import mongo 

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/pokemon')
def pokemonLanding():
    return render_template('pokemonLanding.html')

@app.route('/history')
def historyLanding():
    return render_template('historyLanding.html')

@app.route('/nobel')
def nobelLanding():
    return render_template("nobel.html")

@app.route('/getPokemen', methods=["POST"])
def getMen():

    # connect to DB
    client = pk.connect('69.55.59.139')
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

@app.route('/hist', methods=["POST"])
def retHist():
    # connect
    SERVER_ADDR = "69.55.59.139"  # Aaron
    client = hist.connect(SERVER_ADDR)
    db = client.history
    col = db.files
    hist.imp(db, col)

    date = request.form.get("date")
    phrase = request.form.get("phrase")
    print("\n\n", date, phrase, "\n\n")
    if not date and phrase != "":
        data = hist.find(str(phrase), col)
        if data != -1:
            return render_template("history.html", phrases = data, descs = -1)
    elif date != "" and not phrase:
        data = hist.yearDesc(str(date), col)
        if data[0] != -1:
            return render_template("history.html", phrases = -1, descs = data[1:])
    else:
        if type(date) == type("") and type(phrase) == type(""):
            phrases = hist.find(str(phrase), col)
            dates = hist.yearDesc(str(date), col)
            if phrases != -1 and dates[0] != -1:
                print("\n\n", phrases, "\ndates\n", dates, "\n\n")
                return render_template("history.html", phrases = phrases, descs = dates[1:])

# def getData():
#     type = request.args["type"]
#     data = mongo.getData(request.args["arg"], type)
#     return render_template("result.html", data=data)

# @app.route("/launch")
# def launch():
#     addr = request.args["ip"]
#     mongo.launchDB(addr)
#     return redirect(url_for("nobelLanding"))

if __name__ == '__main__':
    app.debug = True
    app.run()
