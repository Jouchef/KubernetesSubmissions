from database_connection import get_database_connection


def add_default_tasks(connection):
    cursor = connection.cursor()

    default_tasks = [
        ("Osta maitoa", 0),
        ("Tee kotitehtävät", 0),
        ("Siivoa huone", 1),
        ("Käy lenkillä", 0),  
    ]

    cursor.executemany(
        "INSERT INTO tasks (task, done) VALUES (?, ?);",
        default_tasks
    )

    connection.commit()
    print("Added default tasks")


if __name__ == "__main__":
    connection = get_database_connection()
    add_default_tasks(connection)
