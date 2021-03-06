from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), index=True)
    last_name = db.Column(db.String(30), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'Username = {}, Email = {}'.format(self.username, self.email)

class Roles(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64), index=True, unique=True)
    role_desc = db.Column(db.String(120), index=True, unique=True)
    user_role = db.relationship('User_Role',backref='user_Role', lazy='dynamic')

class user_roles(UserMixin, db.Model): #I realize this is not camelcase, but in postgres is written this way
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
