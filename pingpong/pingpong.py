from flask import Flask

app = Flask(__name__)
counter = 0
@app.route('/pingpong')
def pingpong():
    global counter
    response = f"pong {counter}"
    counter += 1
    return response

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", "3003"))
    app.run(host="0.0.0.0", port=port)
