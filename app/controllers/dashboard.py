from flask import render_template, Blueprint, flash, redirect, session
from app.forms import LoginForm
from app import app
from app.models import *

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/')


# @mod_dashboard.route('/')
@mod_dashboard.route('/')
def index():
    return render_template('index.html')