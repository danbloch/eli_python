from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='5vgoY2SmQribsLRFE3xt7jr9cSiEdxhf'
app.config['SQLALCHEMY_DATABSE_URI']='sqlite:///site.db'


from elipython import routes
