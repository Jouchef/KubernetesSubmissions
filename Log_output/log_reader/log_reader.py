from flask import Flask
import os
import requests

app = Flask(__name__)
@app.route("/logs")
def get_pings():

    if not os.path.exists("/app/logs/log.txt"):
        return "log.txt not found", 404
    with open("/app/logs/log.txt", "r") as f:
        timeAndCode = f.read()
        print("File has been read.")
        print(timeAndCode)
        timeAndCode = timeAndCode.replace("\n", "<br>")

    pongs = requests.get(f"http://pingpong-svc:{svc_port}/pingpong").text
    pongs = pongs[5:]

    return f"{timeAndCode} <br> Ping / Pongs: {pongs}"

    
if __name__ == "__main__":
    svc_port = int(os.environ.get("SVC-PORT", "2345"))
    port = int(os.environ.get("PORT", "3004"))
    app.run(host="0.0.0.0", port=port)
