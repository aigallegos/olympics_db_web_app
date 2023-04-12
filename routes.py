""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect
from app import app
from app import database as dbs
#from where_gen import whereGenerator, setGenerator


@app.route("/query1")
def query1():
    

    items = dbs.q1()
    return render_template("a1.html", items=items)
    

@app.route("/query2")
def query2():
    items = dbs.q2()
    return render_template("a2.html", items=items)

@app.route("/athlete")
def Athlete():
    items = dbs.whole_table(0)
    return render_template("athlete.html", items=items)

@app.route("/coach")
def Coach():
    items = dbs.whole_table(1)
    return render_template("coach.html", items=items)

@app.route("/country")
def Country():
    

    items = dbs.whole_table(2)
    return render_template("country.html", items=items)

@app.route("/athlete/delete", methods=['POST'])
def Athlete_delete():
    try:
        json = request.get_json()
        search = json['htmlstr']
        dbs.delete_from_table(search,0)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/coach/delete", methods=['POST'])
def Coach_delete():
    try:
        json = request.get_json()
        search = json['htmlstr']
        dbs.delete_from_table(search,1)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/country/delete", methods=['POST'])
def Country_delete():
    try:
        json = request.get_json()
        search = json['htmlstr']
        dbs.delete_from_table(search,2)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

#searches

@app.route("/athlete/search", methods=['POST'])
def Athlete_search():
    items = ""
    try:
        json = request.get_json()
        search = json['htmlstr']
        items = dbs.filter_from_table(search,0)
        print(items)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return render_template("athlete.html", items=items)

@app.route("/coach/search", methods=['POST'])
def Coach_search():
    items = ""
    try:
        json = request.get_json()
        search = json['htmlstr']
        items = dbs.filter_from_table(search,1)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return render_template("coach.html", items=items)

@app.route("/country/search", methods=['POST'])
def Country_search():
    items = ""
    try:
        json = request.get_json()
        search = json['htmlstr']
        items = dbs.filter_from_table(search,2)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return render_template("country.html", items=items)

@app.route("/athlete/update", methods=['POST'])
def Athlete_update():

    try:
        json = request.get_json()
        search1 = json['htmlstr1']
        search2 = json['htmlstr2']
        dbs.update_db("Athlete",search1,search2)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/coach/update", methods=['POST'])
def Coach_update():

    try:
        json = request.get_json()
        search1 = json['htmlstr1']
        search2 = json['htmlstr2']
        dbs.update_db("Coach",search1,search2)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/country/update", methods=['POST'])
def Country_update():

    try:
        json = request.get_json()
        search1 = json['htmlstr1']
        search2 = json['htmlstr2']
        dbs.update_db("Country",search1,search2)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/athlete/insert", methods=['POST'])
def Athlete_insert():
    json = request.get_json()
    search = json['htmlstr']
    dbs.insert_db("Athlete",search)
    try:
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/country/insert", methods=['POST'])
def Country_insert():
    json = request.get_json()
    search = json['htmlstr']
    dbs.insert_db("Country",search)
    try:
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/coach/insert", methods=['POST'])
def Coach_insert():
    json = request.get_json()
    search = json['htmlstr']
    dbs.insert_db("Coach",search)
    try:
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)