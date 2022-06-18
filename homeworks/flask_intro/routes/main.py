from app import app
from flask import render_template


@app.route('/')
def hello_world():
    a = 'Hello, World!'
    return render_template('index.html', variable=a)


@app.route("/sum/<num1>/<num2>")
def sum(num1, num2):
    result = int(num1) + int(num2)
    return render_template('index.html', variable=result)
