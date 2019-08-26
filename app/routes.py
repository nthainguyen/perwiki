from flask import render_template, flash, redirect, url_for, request
from app.models import User, Entry, Bookmark
from app import app, db, login

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.forms import RegisterFrom, LoginForm, InputForm
from flask_login import current_user, login_user, logout_user, login_required

admin = Admin(app, name='WikiPersonal', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Entry, db.session))
admin.add_view(ModelView(Bookmark, db.session))

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def Register():
    form = RegisterFrom()
    if current_user.is_authenticated:
        return redirect(url_for('Wiki'))
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.create_password(form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', title='Sign up',form=form)

@app.route('/wiki', methods=['POST', 'GET'])
@login_required
def Wiki():
    form = InputForm()
    if form.validate_on_submit():
        entry = Entry(entry_text=form.entry.data, entry_title=form.entry_title.data, author=User.query.get(current_user.id))
        db.session.add(entry)
        db.session.commit()
    return render_template('wiki.html', form=form)

@app.route('/login', methods=['POST','GET'])
def Login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('Wiki'))
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('Login'))
        login_user(user)
        return redirect(url_for('Wiki'))
    return render_template('login.html', form=form)

@app.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('Login'))

@app.route('/add')
@login_required
def AddBookmark():
    url = request.args.get('url')
    title = request.args.get('title')
    bookmark = Bookmark(title=title, link=url, owner=User.query.get(current_user.id))
    db.session.add(bookmark)
    db.session.commit()
    return redirect(url)
