from flask import Flask, request, redirect, Response
from task_reposetory import task_reposetory
from initialize_database import initialize_database
import os

base_url = os.environ.get("BASE_URL", "")

app = Flask(__name__)

@app.route("/todostest", methods=["GET", "POST"])
def tasks():
    if request.method == "GET":
        tasks = task_reposetory.get_all_tasks()
        #print(f"tasks in backend: {tasks}")
        return tasks
    if request.method == "POST":
        data = request.form.get("task")
        if len(data) > 140:
            e_message=(f"Tehtävätekstin maksimipituus on 140 merkkiä. "
                       f"Sinun tekstisi pituus oli: {len(data)}")
            print(e_message)
            return Response(e_message, status=400)
        else:
            print(f"data in request.from.get: {data} "
                f"Data length is: {len(data)}"
                )
            task_reposetory.create_task(data)
            return redirect(f"{base_url}/")


if __name__ == "__main__":
    initialize_database()
    port = int(os.environ.get("BACKEND-PORT", "3007"))
    app.run(host="0.0.0.0", port=port)