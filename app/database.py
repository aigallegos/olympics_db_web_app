from app import db

from app.where_gen import whereGenerator,setGenerator,insertGenerator

# Abram



def q1()->dict: 
    conn = db.connect() 
    query_users_apple = f"""
                        SELECT Country.CCA3, Athlete.name 
                        FROM Athlete INNER JOIN Country ON Athlete.CCA3= Country.CCA3
                        WHERE Country.CCA3 LIKE 'B%%'
                        GROUP BY Country.CCA3, Athlete.name 
                        ORDER BY Athlete.name DESC;
                        """
    query_results=conn.execute(query_users_apple).fetchall()
    conn.close() 
    athlete_items = []
    for result in query_results:
        item = {
            "Country": result[0],
        "Name" : result[1]
        }
        athlete_items.append(item)
    return  athlete_items

def q2()->dict: 
    conn = db.connect() 
    query = f"""
                        SELECT discipline_name 
                        FROM Athlete 
                        UNION
                        SELECT name 
                        FROM (
                        SELECT Discipline.name, Discipline.male_amt, Discipline.female_amt 
                        FROM Discipline 
                        INNER JOIN Athlete ON Athlete.discipline_name = Discipline.name
                        WHERE Athlete.name LIKE 'A%%' AND  Discipline.male_amt > Discipline.female_amt 
                        ) AS derived_table_alias
                        ORDER BY discipline_name DESC"""
    query_results=conn.execute(query).fetchall()
    conn.close() 
    portfolio_items = []
    for result in query_results:
        item = {
            #"DisciplineName": result[0]
            "Username": result[0]
        }
        portfolio_items.append(item)
    return portfolio_items


def delete_from_table(search : str, table : int) -> bool:
    tables = ["Athlete","Coach","Country"]
    whereclause = whereGenerator(search)
    conn = db.connect()
    query = f"Delete From {tables[table]} {whereclause};"
    conn.execute(query)
    conn.close()
    return False

def filter_from_table(search : str, table : int) -> bool:
    tables = ["Athlete","Coach","Country"]
    whereclause = whereGenerator(search)
    conn = db.connect()
    query = f"select * From {tables[table]} {whereclause};"
    print(query)
    results = conn.execute(query).fetchall()
    conn.close()

    items = []
    if table == 0:
        for result in results:
            item = {
                "name": result[0],
                "CCA3" : result[1],
                "discipline_name" : result[2]
            }
            items.append(item)
    elif table == 1:
        for result in results:
            item = {
                "name": result[0],
                "CCA3" : result[1],
                "discipline_name" : result[2],
                "event" : result[3]
            }
            items.append(item)
    else: 
        for result in results:
            item = {
                "CCA3" : result[0],
                "rank_of_population" :result[1],
                "continent" : result[2],
                "population_2020" : result[3],
                "population_2022" : result[4],
                "rank_of_medals" : result[5],
                "num_gold_medals" : result[6],
                "num_silver_medals" : result[7],
                "num_bronze_medls" : result[8],
                "num_total_medals" :result[9]
            }
            items.append(item)
    return  items

def whole_table(table : int) -> bool:
    tables = ["Athlete","Coach","Country"]
    conn = db.connect()
    query = f"select * From {tables[table]};"
    results = conn.execute(query).fetchall()
    conn.close()

    items = []
    if table == 0:
        for result in results:
            item = {
                "name": result[0],
                "CCA3" : result[1],
                "discipline_name" : result[2]
            }
            items.append(item)
    elif table == 1:
        for result in results:
            item = {
                "name": result[0],
                "CCA3" : result[1],
                "discipline_name" : result[2],
                "event" : result[3]
            }
            items.append(item)
    else: 
        for result in results:
            item = {
                "CCA3" : result[0],
                "rank_of_population" :result[1],
                "continent" : result[2],
                "population_2020" : result[3],
                "population_2022" : result[4],
                "rank_of_medals" : result[5],
                "num_gold_medals" : result[6],
                "num_silver_medals" : result[7],
                "num_bronze_medls" : result[8],
                "num_total_medals" :result[9]
            }
            items.append(item)
    return  items


def update_db(table, set_string, where_string):
    conn = db.connect()
    update_query = f"UPDATE {table} {setGenerator(set_string)} {whereGenerator(where_string)};"
    print(update_query)
    conn.execute(update_query)
    conn.close()

def insert_db(table, value_string):

    if table == "Athlete":
        value_string = insertGenerator(value_string,0)
    elif table == "Coach":
        value_string = insertGenerator(value_string,1)
    else:
        value_string = insertGenerator(value_string,2)
    conn = db.connect()
    insert_query = f"INSERT INTO {table} VALUES({value_string});"
    print(insert_query)
    conn.execute(insert_query)
    conn.close()
    
def transaction_db() -> dict:
    conn = db.connect()
    #conn.row_factory = db.Row

    try:
        # Disable auto-commit
        conn.execute("BEGIN")

        # Query 1
        query1 = f"""
                    SELECT Country.CCA3, Athlete.name 
                    FROM Athlete INNER JOIN Country ON Athlete.CCA3= Country.CCA3
                    WHERE Country.CCA3 LIKE 'B%%'
                    GROUP BY Country.CCA3, Athlete.name 
                    ORDER BY Athlete.name DESC;
                    """
        query_results1 = conn.execute(query1).fetchall()

        # Query 2
        query2 = f"""
                    SELECT discipline_name 
                    FROM Athlete 
                    UNION
                    SELECT name 
                    FROM (
                    SELECT Discipline.name, Discipline.male_amt, Discipline.female_amt 
                    FROM Discipline 
                    INNER JOIN Athlete ON Athlete.discipline_name = Discipline.name
                    WHERE Athlete.name LIKE 'A%%' AND  Discipline.male_amt > Discipline.female_amt 
                    ) AS derived_table_alias
                    ORDER BY discipline_name DESC;
                    """
        query_results2 = conn.execute(query2).fetchall()

        # Check requirements and execute additional query
        if len(query_results1) >= 10 and query_results2:
            new_discipline_name = query_results2[0]['discipline_name']
            new_discipline_id = len(query_results2) + 1

            insert_query = f"""
                            INSERT IGNORE INTO Discipline (name)
                            VALUES ('{new_discipline_name}');
                            """
            conn.execute(insert_query)

        # Commit the changes
        conn.execute("COMMIT")

        # Processing results
        athlete_items = []
        for result in query_results1:
            item = {
                "Country": result[0],
                "Name": result[1]
            }
            athlete_items.append(item)

        discipline_items = []
        for result in query_results2:
            item = {
                "DisciplineName": result[0]
            }
            discipline_items.append(item)

    except Exception as e:
        # Rollback changes in case of an exception
        conn.execute("ROLLBACK")
        raise e

    finally:
        # Close the connection
        conn.close()

    return {"athlete_items": athlete_items, "discipline_items": discipline_items}

results = transaction_db()
print(results)
