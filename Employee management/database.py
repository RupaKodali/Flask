from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

