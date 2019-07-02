from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']='5vgoY2SmQribsLRFE3xt7jr9cSiEdxhf'
app.config['SQLALCHEMY_DATABSE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

from elipython import routes
