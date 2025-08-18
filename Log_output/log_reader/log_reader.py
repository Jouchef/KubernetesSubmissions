import time
from flask import Flask
import os

app = Flask(__name__)
@app.route("/logs")
def read_file():
    with open("/app/logs/log.txt", "r") as f:
        content = f.read()
        print("File has been read.")
        print(content)
        response = content.replace("\n", "<br>")
        return response
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "3004"))
    app.run(host="0.0.0.0", port=port)
