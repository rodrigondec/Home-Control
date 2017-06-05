from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class UsuarioForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    is_admin = BooleanField('is_admin', default=False)


class ClientForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])


class ComponentForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    tipo_component = SelectField(u'Tipo Componente', choices=[('Leaf', 'Folha'), ('Modulo', 'Módulo'), ('ModuloPrivado', 'Módulo Privado')])
	

class DispositivoForm(FlaskForm):
    leaf = SelectField('leaf', validators=[DataRequired()])
