from flask import Flask
import os
import requests

app = Flask(__name__)

def get_text_from_file():
    filepath = "/app/config/text_from_file"
    if not os.path.exists(filepath):
        return f"file not found: {filepath}", 404
    with open(filepath) as f:
        text = f.read()
        print(f"text in file was: {text}")

    return text

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

    text_to_show = (f"file content: {get_text_from_file()} <br> "
                    f"env variable: {os.environ.get("MESSAGE", "Error: Could not find the variable")} <br> "
                    f"{timeAndCode} <br> "
                    f"Ping / Pongs: {pongs}")

    return text_to_show

@app.route('/')
def root():
    return "OK", 200

    
if __name__ == "__main__":
    svc_port = int(os.environ.get("SVC-PORT", "2345"))
    port = int(os.environ.get("PORT", "3004"))
    app.run(host="0.0.0.0", port=port)
