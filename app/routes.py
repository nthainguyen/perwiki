from flask import render_template
from app.models import User, Entry
from app import app, db

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.forms import RegisterFrom, LoginForm


admin = Admin(app, name='WikiPersonal', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Entry, db.session))

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def Register():
    form = RegisterFrom()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.create_password(form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', title='Sign up',form=form)

@app.route('/wiki', methods=['POST', 'GET'])
def Wiki():
