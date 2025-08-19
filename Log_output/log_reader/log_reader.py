import time
from flask import Flask
import os

app = Flask(__name__)
@app.route("/logs")
def read_file():
    if not os.path.exists("/app/logs/log.txt"):
        return "log.txt not found", 404
    with open("/app/logs/log.txt", "r") as f:
        timeAndCode = f.read()
        print("File has been read.")
        print(timeAndCode)
        timeAndCode = timeAndCode.replace("\n", "<br>")

    if not os.path.exists("/app/logs/pings.txt"):
        return "pings.txt not found", 404
    with open("/app/logs/pings.txt", "r") as f:
        pings = int(f.read().strip())

    return f"{timeAndCode} <br> ping / pongs: {pings}"

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "3004"))
    app.run(host="0.0.0.0", port=port)
