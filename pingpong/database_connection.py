import psycopg2
import os


DB_HOST = os.environ.get("DB_HOST", "postgres-svc")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "pingpongdb")
DB_USER = os.environ.get("DB_USER", "pingpong")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "secretpassword")

def get_database_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

