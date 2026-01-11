from database_connection import get_database_connection


def add_default_tasks(connection):
    cursor = connection.cursor()

    default_tasks = [
        ("Osta maitoa", True),
        ("Tee kotitehtävät", False),
        ("Siivoa huone", True),
        ("Käy lenkillä", False),  
    ]

    cursor.executemany(
        "INSERT INTO tasks (task, done) VALUES (%s, %s);",
        default_tasks
    )

    connection.commit()
    print("Added default tasks")


if __name__ == "__main__":
    connection = get_database_connection()
    add_default_tasks(connection)
