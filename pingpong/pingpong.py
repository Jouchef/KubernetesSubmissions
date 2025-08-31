import os
from flask import Flask
from initialize_database import initialize_database
from counter_reposetory import counter_reposetory


app = Flask(__name__)
counter = 0


def getCounter():
    global counter
    count = counter_reposetory.get_counter()
    print("count", count)
    counter = int(count) if count else 0
        

def updateCounter():
    global counter
    counter += 1
    counter_reposetory.update_counter(counter)


@app.route('/pingpong')
def pingpong():
    global counter
    getCounter()
    response = f"pong {counter}"
    print(f"pinpong {counter}")
    updateCounter()
    return response

@app.route('/')
def root():
    return "OK", 200

if __name__ == "__main__":
    initialize_database()
    getCounter()
    port = int(os.environ.get("PORT", "3002"))
    app.run(host="0.0.0.0", port=port)
