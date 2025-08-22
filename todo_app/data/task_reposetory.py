from data.database_connection import get_database_connection


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
        except ValueError as e:
            raise ValueError(f"Virhe haettaessa tehtäviä taulusta: {e}") from e
        finally:
            cursor.close()


task_reposetory = TaskReposetory(get_database_connection())