from database_connection import get_database_connection


class TaskReposetory:

    def __init__(self, connection):
        self.connection = connection
    
    def get_all_tasks(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute("SELECT id, task, done FROM tasks")
            rows = cursor.fetchall()

            return [
                {"id": row[0], "task": row[1], "done": row[2]}
                for row in rows
            ]
        except Exception as e:
            self.connection.rollback()
            raise Exception(f"Virhe haettaessa tehtäviä taulusta: {e}") from e
        finally:
            cursor.close()

    def create_task(self, task_name):
        cursor = self.connection.cursor()

        try:
            cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task_name,))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            raise Exception(
            f"Virhe lisätessä tehtävä {task_name} tauluun: {e}") from e
        finally:
            cursor.close()


task_reposetory = TaskReposetory(get_database_connection())