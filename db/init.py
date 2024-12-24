import os
import mysql.connector
from dotenv import load_dotenv

from utils.init_db_query import create_table_query

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}


def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection


def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()
