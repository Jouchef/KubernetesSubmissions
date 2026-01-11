import sys
from database_connection import get_database_connection
from default_data import add_default_tasks


def drop_tables(connection):
    cursor = connection.cursor()
    try:
        cursor.execute('DROP TABLE IF EXISTS tasks;')
        connection.commit()
        print("Tables dropped")
    except Exception as e:
        connection.rollback()
        raise Exception(f"Virhe taulujen poistossa: {e}") from e
    finally:
        cursor.close()



def create_tables(connection):
    cursor = connection.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                task TEXT NOT NULL,
                done BOOLEAN DEFAULT FALSE
            );
        ''')
        connection.commit()
        print("Tables created")
    except Exception as e:
        connection.rollback()
        raise Exception(f"Virhe taulujen luomisessa: {e}") from e
    finally:
        cursor.close()



def table_exists(connection, table_name):
    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name=%s);",
            (table_name.lower(),)
        )
        exists = cursor.fetchone()[0]
        print("Table exists:", exists)
        return exists
    except Exception as e:
        raise Exception(f"Virhe taulun olemassaolon tarkistuksessa: {e}") from e
    finally:
        cursor.close()




def initialize_database(reset: bool = False):
    """
    Alustaa tietokannan tarvittavat taulut ja oletustiedot.

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
    reset_flag = len(sys.argv) > 1 and sys.argv[1].lower().lstrip('-') == "reset"
    initialize_database(reset=reset_flag)
