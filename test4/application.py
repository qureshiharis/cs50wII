from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():

    name = request.form.get("name")

    if request.method == "POST":
        return f"Hello {name}"
    else:
        return render_template("index.html")
