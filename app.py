from flask import Flask, render_template, request, session, redirect, url_for, make_response
import jinja2

app = Flask(__name__)
app.secret_key = b"batman"

@app.route('/')
def home():
    return render_template("hello_world.html")

@app.route('/name')
def name():
    return render_template("name.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
