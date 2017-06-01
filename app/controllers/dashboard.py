from flask import render_template, Blueprint, flash, redirect, session, url_for
from app.forms import LoginForm
from app.models import *

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@mod_dashboard.route('/')
def index():
    if 'logged_in' in session:
        print(session['logged_in'])
    return render_template('index.html')


@mod_dashboard.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        session['logged_in'] = True
        return redirect(url_for('dashboard.index'))
    return render_template('login.html', title='Sign In', form=form)

@mod_dashboard.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('dashboard.index'))


@mod_dashboard.route('/oi')
def oi():
    return 'TESTE'
