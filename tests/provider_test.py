import unittest
from flask import Flask
from flash_sqlalchemy import SQLAlchemy
from provider import db
from provider import regex

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  ''

db = SQLAlchemy(app)
db.create_all()
def dbSetup():
    db.create_all()


def dbTeardown():
    db.drop_all()

def buildTestReg():
    test_reg = Regex('abcdefg')
    db.session.add(test_reg)
    db.session.commit()

class RegexModelTest(unittest.TestCase):
    def test_regex(self):
        test_reg = Regex('abcdefg')
        self.assertEqual(test_reg.regex, 'abcdefg')
