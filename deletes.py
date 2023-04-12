#deletes


@app.route("/Athlete/delete/<search>", methods=['POST'])
def delete(search):
    """ recieved post requests for entry delete """
    try:
        db_helper.delete_from_table(search,0)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/Coach/delete/<search>", methods=['POST'])
def delete(search):
    """ recieved post requests for entry delete """
    try:
        db_helper.delete_from_table(search,1)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/Country/delete/<search>", methods=['POST'])
def delete(search):
    """ recieved post requests for entry delete """
    try:
        db_helper.delete_from_table(search,2)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

#searches

@app.route("/Athlete/search/<search>", methods=['GET'])
def delete(search):
    """ recieved post requests for entry delete """
    try:
        db_helper.filter_from_table(search,0)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/Coach/search/<search>", methods=['GET'])
def delete(search):
    """ recieved post requests for entry delete """
    try:
        db_helper.filter_from_table(search,1)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)

@app.route("/Country/search/<search>", methods=['GET'])
def delete(search):
    """ recieved post requests for entry delete """
    try:
        db_helper.filter_from_table(search,2)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    print(result)
    return jsonify(result)


#-------------------------------------------------------------------------------------

def filter_from_table(search : str, table : int) -> bool:
    tables = ["Athlete","Coach","Country"]
    whereclause = whereGenerator(search)
    conn = db.connect()
    query = f"select * From {tables[table]} {whereclause};"
    conn.execute(query)
    conn.close()
    return False

def delete_from_table(search : str, table : int) -> bool:
    tables = ["Athlete","Coach","Country"]
    whereclause = whereGenerator(search)
    conn = db.connect()
    query = f"Delete From {tables[table]} {whereclause};"
    conn.execute(query)
    conn.close()
    return False
