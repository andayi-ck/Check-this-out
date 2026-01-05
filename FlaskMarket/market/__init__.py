import sqlite3

from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

from flask_mail import Mail




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/ADMIN/.vscode/.vscode/FlaskMarket/market.db'
app.config['SECRET_KEY'] = '8ad23f8c1fc35fb1668cff85'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(weeks=365000)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
mail = Mail(app)


login_manager.login_view = "login_page"  # Redirects users to login if not logged in
login_manager.login_message_category = "info"
from market import routes
