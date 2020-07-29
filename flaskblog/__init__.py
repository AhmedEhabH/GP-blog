from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_mongoalchemy import MongoAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b61193399df06673c88d402db7a45759'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['MONGOALCHEMY_DATABASE'] = 'mongodb+srv://ahmedehab:Password@quiz-hvhc1.gcp.mongodb.net/GP?retryWrites=true&w=majority'
db = SQLAlchemy(app)
# db = MongoAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
