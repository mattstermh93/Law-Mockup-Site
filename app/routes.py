from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index', methods=['GET', 'PUT'])
def index():
    return render_template("index.html", title='Home Page')