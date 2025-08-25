import time
from flask import Flask, render_template
import os
import requests
import threading


app = Flask(__name__)

imagePath = "static/images/kuva.jpg"
cacheTime = 600 #Seconds

pictureUrl = "https://picsum.photos/300/200.jpg"

download_lock = threading.Lock()

def get_pic():
    if not os.path.exists(imagePath):
         print(f"No image detected in the filepath {imagePath}")
         os.makedirs(os.path.dirname(imagePath), exist_ok=True)
         download_pic()
    else:
        cachedTime = time.time() - os.path.getmtime(imagePath)
        print(f"The picture in {imagePath} has been cached for {cachedTime} seconds. The limit is {cacheTime}")
        if cachedTime > cacheTime:
            if not download_lock.locked(): 
                print("Cache expired. Refreshing in thread...")
                threading.Thread(target=download_pic, daemon=True).start()
            else:
                print("Download already in progress, skipping new request.")


def download_pic():
        with download_lock:
            print("Requesting a new picture!")
            data = requests.get(pictureUrl).content

            with open(imagePath, "wb") as f:
                f.write(data)


@app.route("/")
def homepage():
    get_pic()
    tasks = requests.get("http://backend-svc:2345/todos").json()
    print(f"tasks: {tasks}")
    return render_template("index.html", tasks=tasks)



if __name__ == "__main__":
    port = int(os.environ.get("FRONT-PORT", "5000"))
    app.run(host="0.0.0.0", port=port)