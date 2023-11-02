from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired

class UserRegisterForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    username = StringField('Username')
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class UserLoginForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class UserUpdateForm(FlaskForm):
    profile_pic = FileField('Profile Picture')
    username = StringField('Username')
    submit = SubmitField('Update')
