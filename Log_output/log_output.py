import random
import string
import time
from flask import Flask, jsonify
import threading
import os

app = Flask(__name__)

status = {
    "time": None,
    "random_string": None
}

def gen_rand_str(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def update_status():
    while True:
        length = 10
        status["random_string"] = gen_rand_str(length)
        status["time"] = time.strftime("%H:%M:%S", time.localtime())
        print(status["time"], status["random_string"])
        time.sleep(5)

@app.route("/")
def get_status():
    return jsonify(status)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    t = threading.Thread(target=update_status, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=port)

