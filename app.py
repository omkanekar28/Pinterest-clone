from blogproject import app
from flask import render_template, session, flash, redirect, url_for
from blogproject import db

@app.route('/')
def index():
    try:
        session['email']
    except KeyError:
        flash("Please log in first!")
        return redirect(url_for('users.login'))
    return render_template('index.html')

@app.route('/about')
def about():
    try:
        session['email']
    except KeyError:
        flash("Please log in first!")
        return redirect(url_for('users.login'))
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)