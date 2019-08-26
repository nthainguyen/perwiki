from app import app, db, login
from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(60), index=True)
    entry = db.relationship('Entry', backref='author', lazy='dynamic')
    bookmark = db.relationship('Bookmark', backref='owner', lazy='dynamic')
    email = db.Column(db.String(70))
    password_hash = db.Column(db.String(256))

    def create_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    entry_title = db.Column(db.String(150), index=True)
    entry_text = db.Column(db.String(1000), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Entry {}>".format(self.entry_title)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(200), index=True)
    link = db.Column(db.String(200), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Bookmark {}>".format(self.title)
