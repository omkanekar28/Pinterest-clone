from blogproject import db
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default="default_profile.png")
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Blog', backref='author', lazy=True)


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(password=password)


    def __repr__(self):
        return f"Username: {self.username}"


    def check_password(self, password):
        is_valid = bcrypt.check_password_hash(self.password_hash, password)
        return is_valid


class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    image = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))
    uploaded_on = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __init__(self, image, title, description, user_id):
        self.image = image
        self.title = title
        self.description = description
        self.user_id = user_id
        self.uploaded_on = datetime.now()
    
    