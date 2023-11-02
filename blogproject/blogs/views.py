from flask import render_template, Blueprint, session, flash, redirect, url_for, request
from .forms import BlogUploadForm
from blogproject.models import User, Blog
import os
from blogproject import UPLOAD_FOLDER, db


blogs_blueprint = Blueprint('blogs', __name__, template_folder='templates/blogs')


@blogs_blueprint.route('/')
def allblogs():
    try:
        session['email']
    except KeyError:
        flash("Please log in first!")
        return redirect(url_for('users.login'))

    blogs = Blog.query.all()
    authors = []
    for blog in blogs:
        user = User.query.get(blog.user_id)
        authors.append(user.username)
    return render_template('allblogs.html', blogs=blogs, authors=authors)


@blogs_blueprint.route('/add', methods=['POST', 'GET'])
def add():
    try:
        session['email']
    except KeyError:
        flash("Please log in first!")
        return redirect(url_for('users.login'))

    form = BlogUploadForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        user = User.query.filter_by(email=session['email']).first()
        image = request.files['image']
        filename = image.filename.replace(' ', '_')
        ext = filename.split('.')[1]
        if ext not in ('jpg', 'png'):
            flash("Only jpg or png files are allowed!")
            return redirect(url_for('index'))
        image_path = os.path.join('blogimages', filename)
        blog = Blog(image=image_path, title=title, description=description, user_id=user.id)
        db.session.add(blog)
        db.session.commit()
        image.save(os.path.join(UPLOAD_FOLDER, 'blogimages', filename))
        flash('Blog posted successfully')
        return redirect(url_for('blogs.add'))
        
    return render_template('add.html', form=form)