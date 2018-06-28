from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index', methods=['GET', 'PUT'])
def index():
    return render_template("index.html", title='Home Page')

@app.route('/who', methods=['GET', 'PUT'])
def who():
    return render_template("who.html", title='Who We Are')

@app.route('/what', methods=['GET', 'PUT'])
def what():
    return render_template("what.html", title='What We Do')

@app.route('/news', methods=['GET', 'PUT'])
def news():
    return render_template("news.html", title='News and Events')

@app.route('/where', methods=['GET', 'PUT'])
def where():
    return render_template("where.html", title='Where We Work')

@app.route('/contact', methods=['GET', 'PUT'])
def contact():
    return render_template("contact.html", title='Contact Us')
