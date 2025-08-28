from database_connection import get_database_connection


class CounterReposetory:

    def __init__(self, connection):
        self.connection = connection

    def get_counter(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute("SELECT value FROM counter WHERE id=1")
            row = cursor.fetchone()

            return row[0] if row else 0
        
        except Exception as e:
            raise Exception(f"Virhe haettaessa laskuria taulusta: {e}") from e
        finally:
            cursor.close()

    def update_counter(self, new_value):
        cursor = self.connection.cursor()

        try:
            cursor.execute("UPDATE counter SET value=%s WHERE id=1", (new_value,))
            self.connection.commit()
            return True
        except Exception as e:
            raise Exception(f"Virhe lisättäessä arvoa tauluun: {e}") from e
        finally:
            cursor.close()



counter_reposetory = CounterReposetory(get_database_connection())