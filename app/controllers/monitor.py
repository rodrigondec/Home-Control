from flask import render_template, Blueprint, session, abort, flash, redirect, url_for

mod_monitor = Blueprint('monitor', __name__, url_prefix='/monitor', template_folder='templates')
# @TODO fazer metodos controlador monitor
# @TODO fazer views monitor
