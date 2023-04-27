from app import db

from app.where_gen import whereGenerator,setGenerator,insertGenerator

# Abram



def q1(starting_letters:str)->dict: 
    conn = db.connect() 
    query_users_apple = f"""
                        SELECT Country.CCA3, Athlete.name 
                        FROM Athlete INNER JOIN Country ON Athlete.CCA3= Country.CCA3
                        WHERE Country.CCA3 LIKE '{starting_letters}%%'
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

def q2(starting_letters:str)->dict: 
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
                        WHERE Athlete.name LIKE '{starting_letters}%%' AND  Discipline.male_amt > Discipline.female_amt 
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
    conn = db.connect(isolation_level='READ COMMITTED')
    update_query = f"UPDATE {table} {setGenerator(set_string)} {whereGenerator(where_string)};"
    print(update_query)
    conn.execute(update_query)
    conn.close()

def transaction_db(country_code, discipline_name) -> dict:
    conn = db.connect(":memory:")  # Use an in-memory SQLite database for demonstration
    conn.row_factory = db.Row

    try:
        # Disable auto-commit
        conn.execute("BEGIN")

        # Query 1: Find athletes from a certain country and discipline
        query1 = f"""
                    SELECT Athlete.name, Country.CCA3, Discipline.name AS discipline_name
                    FROM Athlete
                    INNER JOIN Country ON Athlete.CCA3 = Country.CCA3
                    INNER JOIN Discipline ON Athlete.discipline_name = Discipline.name
                    WHERE Country.CCA3 = ? AND Discipline.name = ?;
                    """
        query_results1 = conn.execute(query1, (country_code, discipline_name)).fetchall()

        # Query 2: Find coaches from a certain country and discipline
        query2 = f"""
                    SELECT Coach.name, Country.CCA3, Discipline.name AS discipline_name
                    FROM Coach
                    INNER JOIN Country ON Coach.CCA3 = Country.CCA3
                    INNER JOIN Discipline ON Coach.discipline_name = Discipline.name
                    WHERE Country.CCA3 = ? AND Discipline.name = ?;
                    """
        query_results2 = conn.execute(query2, (country_code, discipline_name)).fetchall()

        # Check requirements and execute additional query
        if query_results1 and query_results2:
            athlete_name = query_results1[0]['name']
            coach_name = query_results2[0]['name']

            insert_query = f"""
                            INSERT INTO Athlete_Coach (athlete_name, coach_name)
                            VALUES (?, ?);
                            """
            conn.execute(insert_query, (athlete_name, coach_name))

        # Commit the changes
        conn.execute("COMMIT")

        # Processing results
        athlete_items = []
        for result in query_results1:
            item = {
                "Name": result[0],
                "Country": result[1],
                "Discipline": result[2]
            }
            athlete_items.append(item)

        coach_items = []
        for result in query_results2:
            item = {
                "Name": result[0],
                "Country": result[1],
                "Discipline": result[2]
            }
            coach_items.append(item)

    except Exception as e:
        # Rollback changes in case of an exception
        conn.execute("ROLLBACK")
        raise e

    finally:
        # Close the connection
        conn.close()

    return {"athlete_items": athlete_items, "coach_items": coach_items}

results = transaction_db("USA", "Swimming")
print(results)
