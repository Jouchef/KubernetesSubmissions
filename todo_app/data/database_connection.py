import os
import sqlite3

dirname = os.path.dirname(__file__)

db_path = os.path.join(dirname, "db", "database.sqlite")

os.makedirs(os.path.dirname(db_path), exist_ok=True)

connection = sqlite3.connect(db_path, check_same_thread=False)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection