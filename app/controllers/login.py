
from flask import render_template, Blueprint, flash, redirect, session
from app.forms import LoginForm
from app import app
from app.models import *

mod_login = Blueprint('login', __name__, url_prefix='/login')


@mod_login.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        session['logged_in'] = True
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)

@mod_login.route('/out', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')