from flask import Flask, request, redirect
from task_reposetory import task_reposetory
from initialize_database import initialize_database
import os


app = Flask(__name__)

@app.route("/todos", methods=["GET", "POST"])
def tasks():
    if request.method == "GET":
        tasks = task_reposetory.get_all_tasks()
        print(f"tasks in backend: {tasks}")
        return tasks
    if request.method == "POST":
        data = request.form.get("task")
        print(f"data in request.from.get: {data}")
        task_reposetory.create_task(data)
        return redirect("/")


if __name__ == "__main__":
    initialize_database()
    port = int(os.environ.get("BACKEND-PORT", "3007"))
    app.run(host="0.0.0.0", port=port)