from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField
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
    tipo_component = SelectField(u'Tipo Componente',
                                 choices=[('Leaf', 'Folha'), ('Modulo', 'Módulo'), ('ModuloPrivado', 'Módulo Privado')])
	

class DispositivoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    porta = IntegerField('porta', validators=[DataRequired()])
    tipo_dispositivo = SelectField(u'Tipo Dispositivo',
                                 choices=[('Sensor', 'Sensor'), ('Interruptor', 'Interruptor'), ('Potenciometro', 'Potenciômetro')])


class EmbarcadoForm(FlaskForm):
    ip = StringField('ip', validators=[DataRequired()])
    mac = StringField('mac', validators=[DataRequired()])


class MonitorForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    tipo_monitor = SelectField(u'Tipo Monitor',
                                 choices=[('MonitorManual', 'Monitor Manual'), ('MonitorAutomatico', 'Monitor Automático')])
