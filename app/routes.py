from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index', methods=['GET', 'PUT'])
def index():
    return render_template("index.html", title='Home Page')

@app.route('/redirect')
def goaway():
    return redirect(url_for('index'))

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid login credentials')
            return redirect(url_for('login'))
        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        flash('Thanks for logging in {}!'.format(current_user.username))
        return redirect(next_page)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        user = User(username=register_form.username.data, email=register_form.email.data)
        user.set_password(register_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! You can now view your profile.')
        return redirect(url_for('login'))
    return render_template('register.html', form=register_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'PUT'])
def profile():
    return render_template("profile.html", title='Profile')

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    return render_template('edit_profile.html', title='Edit Profile', form=form)
