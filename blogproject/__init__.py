from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

UPLOAD_FOLDER = os.path.join(basedir, 'static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

from blogproject.users.views import users_blueprint
from blogproject.blogs.views import blogs_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(blogs_blueprint, url_prefix='/blogs')
