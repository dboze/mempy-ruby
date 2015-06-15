from flask import Flask
from flask import request
import time

app = Flask(__name__)

@app.route("/")
def nap():
    time.sleep(float(request.args.get("sec")))
    return request.args.get("msg")

if __name__ == "__main__":
    app.run(port=4567)
