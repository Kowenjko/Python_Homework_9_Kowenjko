import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import *

try:
    connection = psycopg2.connect(user=USER,
                                  password=PASSWORD,
                                  host=HOST,
                                  port=PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    sql_create_database = 'CREATE DATABASE user_db'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Error while working with PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed")
