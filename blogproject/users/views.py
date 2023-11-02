from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from blogproject.models import User
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from blogproject import db
from blogproject import UPLOAD_FOLDER
import os

users_blueprint = Blueprint('users', __name__, template_folder='templates/users')


@users_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    try:
        session['email']
    except KeyError:
        pass
    else:
        flash("Please log out first!")
        return redirect(url_for('index'))
    
    form = UserRegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            flash("Password fields don't match!")
            return redirect(url_for('users.register'))
        user = User.query.filter_by(email=email)
        try:
            user = user[0]
        except IndexError:
            user = User(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            session['email'] = email
            return redirect(url_for('index'))
        else:
            flash("An account already exists with this Email ID!")
            return redirect(url_for('users.register'))
    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    try:
        session['email']
    except KeyError:
        pass
    else:
        flash("Please log out first!")
        return redirect(url_for('index'))

    form = UserLoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email)
        try:
            user = user[0]
        except IndexError:
            flash("Incorrect Email!")
            return redirect(url_for('users.login'))
        else:
            if user.check_password(password):
                session['email'] = email
                return redirect(url_for('index'))
            flash("Incorrect password!")
            return redirect(url_for('users.login'))  
    return render_template('login.html', form=form)


@users_blueprint.route('/logout', methods=['POST', 'GET'])
def logout():
    try:
        session['email']
    except KeyError:
        flash("You are already logged out")
        return redirect(url_for('users.login'))
    session.pop('email')
    return redirect(url_for('users.login'))


@users_blueprint.route('/account', methods=['POST', 'GET'])
def account():

    try:
        session['email']
    except KeyError:
        flash("Please log in first!")
        return redirect(url_for('users.login')) 

    form = UserUpdateForm()
    user = User.query.filter_by(email=session['email']).first()

    if form.validate_on_submit():      
        
        if form.username.data:
            user.username = form.username.data
            print(user.username)
            db.session.add(user)
            db.session.commit()
        if form.profile_pic.data:
            image = request.files['profile_pic']
            filename = image.filename.replace(' ', '_')
            ext = filename.split('.')[1]
            if ext not in ('jpg', 'png'):
                flash("Only jpg or png files are allowed!")
                return redirect(url_for('users.account'))
            image.save(os.path.join(UPLOAD_FOLDER, 'profileimages', filename))
            user.profile_image = os.path.join('profileimages', filename)
            db.session.add(user)
            db.session.commit()
            flash("Profile picture uploaded successfully")
            return redirect(url_for('users.account'))    
    return render_template('account.html', form=form, user=user)