from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("VERSION", "v1")

@app.route("/")
def home():
    return f"Hello DevOps! Version: {VERSION}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)