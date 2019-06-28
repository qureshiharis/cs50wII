from flask import Flask, render_template, request

app = Flask(__name__)

names = []

@app.route("/", methods=["GET", "POST"])
def index():
    # If sending information from page (POST)
    if request.method == "POST":

        # Get information entered in html
        name = request.form.get("name")
        names.append(name)

        return render_template("index.html", names=names)

    # If accessing information from page (GET)
    else:
        return render_template("index.html")
