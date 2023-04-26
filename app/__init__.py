"""Setup at app startup"""
import os
import sqlalchemy
from flask import Flask
from yaml import load, Loader



def init_connection_engine():

    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os._exit(1)

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST'),
            query={
            "unix_socket": "/cloudsql/{}".format(os.environ.get('INSTANCE_CONNECTION_NAME'))
            }
        )
    )

    return pool


app = Flask(__name__)
db = init_connection_engine()

from app import routes
