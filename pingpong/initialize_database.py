from database_connection import get_database_connection


def initialize_database():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS counter (
            id SERIAL PRIMARY KEY,
            value INT NOT NULL
        )
    """)
    # jos tyhjä, lisää alkuluku
    cursor.execute("SELECT COUNT(*) FROM counter")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO counter (value) VALUES (0)")
        print("Counter table was not iintialized. Added 0 as starting point.")
    connection.commit()
    cursor.close()
    connection.close()
