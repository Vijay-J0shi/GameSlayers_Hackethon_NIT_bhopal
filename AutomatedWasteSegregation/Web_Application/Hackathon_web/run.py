from flask import Flask, request, render_template, url_for, redirect,jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")



if __name__ == "__main__":  # used to run directly python module
    app.run(debug=True)
