from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

WebIFace = Flask(__name__)

mysql = MySQL()

WebIFace.config['MYSQL_DATABASE_USER'] = 'dcord'
WebIFace.config['MYSQL_DATABASE_PASSWORD'] = 'dcord'
WebIFace.config['MYSQL_DATABASE_DB'] = 'DiscordApp'
WebIface.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(WebIFace)

conn = mysql.connect()
cursor = conn.cursor()

class DAPIModel(db.Model):
    id = db.Column(db

DISCORD_ROUTE = "/dapi/"
DAPI_SEND = DISCORD_ROUTE + "send"
DAPI_CONFIG = DISCORD_ROUTE + "config"
DAPI_GETMSG = DISCORD_ROUTE + "getmsg"
DAPI_ADDREG = DISCORD_ROUTE + "addreg"
DAPI_GETREG = DISCORD_ROUTE + "getreg"
DAPI_DELREG = DISCORD_ROUTE + "delreg"
DAPI_LISTREG = DISCORD_ROUTE + "listreg"

TODO = 'notimplemented.html'

@WebIFace.route("/")
def index():
    return render_template('index.html')

@WebIFace.route(DAPI_SEND, methods=['POST'])
def send():
    message = _request.form['message']

@WebIFace.route(DAPI_GETMSG)
def getmsg():
    return render_template(TODO)

@WebIFace.route(DAPI_CONFIG)
def getconfig():
    return render_template(TODO)


regtblname = "Discordreg"
SQL_LIST_REG = "SELECT * FROM " + regtblname + " LIMIT {quantity:d}"#.format (startid=?, quantity=?)
SQL_DEL_REG = "DELETE FROM " + regtblname + " where regid = '{regid:d}'"#.format (regid=?)
SQL_GET_REG = "SELECT * FROM " + regtblname + " where reg id = '{regid:d}'" #.format(regid=?)
SQL_INSERT_INTO = "INSERT INTO Discordreg (regex) VALUES ('{regex}')" #.format(regex=?)

@WebIFace.route(DAPI_ADDREG, methods=['POST'])
def addreg():
    regex = _request.form['regid']
    regex_str = request.form['regex']
    cursor.execute(SQL_INSERT_INTO)

@WebIFace.route(DAPI_GETREG, methods=['POST'])
def getreg():
    regex = _request.form['regid']
    cursor.execute(SQL_GET_REG)

@WebIFace.route(DAPI_DELREG, methods=['POST'])
def delreg():
    regex = _request.form['regid']
    cursor.execute(SQL_DEL_REG)

@WebIFace.route(DAPI_LISTREG, methods=['POST'])
def listreg():
    getnum = _request.form['quantity']
    startid = _request.form['startid']
    cursor.execute(SQL_LIST_REG)


@WebIFace.teardown_appcontext
def close_connection(exception):
    pass
#   if mysql is not None:
#        mysql.close()
