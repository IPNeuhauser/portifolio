import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))