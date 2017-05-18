from flask import render_template, Blueprint
from app import app, dados
from app.models import *

@app.route('/')
def index():
	print(dados)
	user = {'nickname': 'Miguel'}
	return render_template('index.html', title='Home', user=user)

mod_propriedade = Blueprint('propriedade', __name__, url_prefix='/propriedade')

@mod_propriedade.route('/')
def propriedade_index():
	return "propriedade index"