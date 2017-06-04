from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])