from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/<string:name>")
def greeting(name):
    return f"Hello, {name}!"
