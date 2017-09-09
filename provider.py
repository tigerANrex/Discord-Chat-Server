from flask import Flask
from flash_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  ''
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Regex(db.Model):
    regid = db.Column(db.Integer, primary_key=True)
    regex = db.Column(db.String(80), unique=True)
    user = db.relationship('User',
                           backref=db.backref('User', lazy='dynamic'))

    def __init__(self, regex):
        self.regex = regex

    def __repr__(self):
        return '<Regex %r>' % self.regex
