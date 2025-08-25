import sys
from database_connection import get_database_connection
from default_data import add_default_tasks


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS tasks;')
    connection.commit()
    print("Tables dropped")


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done BOOLEAN DEFAULT 0
        );
    ''')
    connection.commit()
    print("Tables created")


def table_exists(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
        (table_name,)
    )
    result = cursor.fetchone()
    print("result:", result)
    cursor.close()
    return result is not None


def initialize_database(reset: bool = False):
    """
    Alustaa SQLite-tietokannan tarvittavat taulut ja oletustiedot.

    Args:
        reset (bool): Jos True, poistaa olemassa olevat taulut ja luo ne uudelleen
                      oletustietoineen. Jos False, tarkistaa onko taulu 'tasks'
                      jo olemassa ja luo sen, jos sitä ei ole.
    """
    connection = get_database_connection()

    if reset:
        drop_tables(connection)
        create_tables(connection)
        add_default_tasks(connection)
        print("Database reset complete")
    else:
        if not table_exists(connection, "tasks"):
            create_tables(connection)
            add_default_tasks(connection)
            print("Database initialized")
        else:
            print("Database already exists, skipping initialization.")


if __name__ == "__main__":
    reset_flag = len(sys.argv) > 1 and sys.argv[1].lower() == "reset"
    initialize_database(reset=reset_flag)
