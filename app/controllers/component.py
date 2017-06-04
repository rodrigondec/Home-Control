from flask import render_template, Blueprint, session, abort, flash, redirect, url_for
from app import app
from app.models import *

mod_component = Blueprint('component', __name__, url_prefix='/component', template_folder='templates')
# @TODO fazer metodos controlador component
# @TODO fazer views component

@mod_component.route('/')
def index():
    return "component index"


def listar_modulos():
    pass


def listar_dispositivos():
    pass


def alterar_interruptor():
    pass


def alterar_potenciometro():
    pass
