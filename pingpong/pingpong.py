import os
from flask import Flask

app = Flask(__name__)
counter = 0

path = "/app/logs/pings.txt"

def getCounter():
    global counter
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("0")
            return
    with open(path, "r") as f:
        content = f.read().strip()
        counter = int(content) if content else 0
        

def updateCounter():
    global counter
    counter += 1
    with open(path, "w") as f:
        f.write(f"{counter}")


@app.route('/pingpong')
def pingpong():
    global counter
    getCounter()
    response = f"pong {counter}"
    updateCounter()
    return response

if __name__ == "__main__":
    getCounter()
    port = int(os.environ.get("PORT", "3003"))
    app.run(host="0.0.0.0", port=port)
