from flask import Flask, render_template, request, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = b"batman"

@app.route('/')
def home():
    return "Hello, World!"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
