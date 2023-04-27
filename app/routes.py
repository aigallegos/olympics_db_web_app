""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, render_template_string
from app import app
from app import database as dbs
#from where_gen import whereGenerator, setGenerator


@app.route("/query1/<search>")
def query1(search):
    items = dbs.q1(search)
    return render_template("a1.html", items=items)

@app.route('/transaction/<country_code>/<discipline_name>')
def transaction_route(country_code, discipline_name):
    results = dbs.transaction_db(country_code, discipline_name)
    return render_template("transaction_results.html", results=results)
    

@app.route("/query2/<search>")
def query2(search):
    items = dbs.q2(search)
    return render_template("a2.html", items=items)

@app.route("/")
def root():
    items = dbs.whole_table(0)
    return render_template("athlete.html", items=items)

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

@app.route("/athlete/search", methods=['GET'])
def Athlete_search():
    search_text = request.args.get('search_text')

    items = dbs.filter_from_table(search_text,0)

    rendered_template = render_template_string('<table class="table"><thead><tr><th class="athlete-name">Athlete Name</th><th class="country-cca3">Country CCA3</th><th class="disciple-name">Discipline Name</th></tr></thead><tbody>{% for item in items %}<tr><td>{{item.name}}</td><td>{{item.CCA3}}</td><td>{{item.discipline_name}}</td></tr>{% endfor %}</tbody></table>', items=items)
    return rendered_template


@app.route("/coach/search", methods=['GET'])
def Coach_search():
    search_text = request.args.get('search_text')

    items = dbs.filter_from_table(search_text,1)

    rendered_template = render_template_string('<table class="table"><thead><tr><th class="athlete-name">Athlete Name</th><th class="country-cca3">Country CCA3</th><th class="disciple-name">Discipline Name</th></tr></thead><tbody>{% for item in items %}<tr><td>{{item.name}}</td><td>{{item.CCA3}}</td><td>{{item.discipline_name}}</td></tr>{% endfor %}</tbody></table>', items=items)
    return rendered_template

@app.route("/country/search", methods=['GET'])
def Country_search():
    search_text = request.args.get('search_text')

    items = dbs.filter_from_table(search_text,2)

    rendered_template = render_template_string('<table class="table"><thead><tr><th class="athlete-name">Athlete Name</th><th class="country-cca3">Country CCA3</th><th class="disciple-name">Discipline Name</th></tr></thead><tbody>{% for item in items %}<tr><td>{{item.name}}</td><td>{{item.CCA3}}</td><td>{{item.discipline_name}}</td></tr>{% endfor %}</tbody></table>', items=items)
    return rendered_template

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
