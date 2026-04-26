from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("VERSION", "v2")

@app.route("/")
def home():
    return f"Hello this is my DevOps project Version: {VERSION}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)