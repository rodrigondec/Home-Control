from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField, FloatField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, NumberRange
from app.models import Dispositivo


class LoginForm(FlaskForm):
    email = EmailField(u'Email', validators=[DataRequired()])
    senha = PasswordField(u'Senha', validators=[DataRequired()])


class UsuarioForm(FlaskForm):
    nome = StringField(u'Nome', validators=[DataRequired()])
    email = EmailField(u'Email', validators=[DataRequired()])
    senha = PasswordField(u'Senha', validators=[DataRequired()])
    is_admin = BooleanField(u'Administrador', default=False)


class ClientForm(FlaskForm):
    nome = StringField(u'Nome', validators=[DataRequired()])


class ComponentForm(FlaskForm):
    nome = StringField(u'Nome', validators=[DataRequired()])
    tipo_component = SelectField(u'Tipo Componente',
                                 choices=[('Leaf', 'Folha'), ('Modulo', 'Módulo Público'), ('ModuloPrivado', 'Módulo Privado')])
	

class DispositivoForm(FlaskForm):
    nome = StringField(u'Nome', validators=[DataRequired()])
    porta = IntegerField(u'Porta', validators=[DataRequired()])
    tipo_dispositivo = SelectField(u'Tipo Dispositivo',
                                 choices=[('Sensor', 'Sensor'), ('Interruptor', 'Interruptor'), ('Potenciometro', 'Potenciômetro')])


class EmbarcadoForm(FlaskForm):
    ip = StringField(u'Ip', validators=[DataRequired()])
    mac = StringField(u'Mac', validators=[DataRequired()])


class MonitorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    tipo_monitor = SelectField(u'Tipo Monitor',
                                 choices=[('MonitorManual', 'Monitor Manual'), ('MonitorAutomatico', 'Monitor Automático')])


class RegraTipoDispositivoForm(FlaskForm):
    form_name = HiddenField('regra_tipo_dispositivo', default='regra_tipo_dispositivo')
    tipo_dispositivo = SelectField(u'Tipo Dispositivo', validators=[DataRequired()], choices=[('Sensor', 'Sensor'), ('Interruptor', 'Interruptor'), ('Potenciometro', 'Potenciômetro')])


class RegraInterruptorForm(FlaskForm):
    form_name = HiddenField('regra_interruptor')
    tipo_dispositivo = HiddenField('Tipo Dispositivo')
    valor = BooleanField('Ligado')
    cronometrado = BooleanField('Cronometrado', default=False)
    hora = IntegerField('Hora', validators=[NumberRange(min=00, max=23)])
    minuto = IntegerField('Minuto', validators=[NumberRange(min=00, max=60)])

    def __init__(self, tipo_dispositivo):
        super(RegraInterruptorForm, self).__init__()
        self.tipo_dispositivo.data = tipo_dispositivo


class RegraPotenciometroForm(FlaskForm):
    form_name = HiddenField('regra_potenciometro')
    tipo_dispositivo = HiddenField('Tipo Dispositivo')
    valor = FloatField('Valor', validators=[DataRequired()])
    cronometrado = BooleanField('Cronometrado', default=False)
    hora = IntegerField('Hora', validators=[NumberRange(min=00, max=23)])
    minuto = IntegerField('Minuto', validators=[NumberRange(min=00, max=60)])

    def __init__(self, tipo_dispositivo):
        super(RegraPotenciometroForm, self).__init__()
        self.tipo_dispositivo.data = tipo_dispositivo


class RegraSensorForm(FlaskForm):
    form_name = HiddenField('regra_sensor')
    tipo_dispositivo = HiddenField('Tipo Dispositivo')
    valor_inicial = FloatField('Valor inicial', validators=[DataRequired()])
    valor_final = FloatField('Valor inicial', validators=[DataRequired()])
    atuador = SelectField('Atuador', validators=[DataRequired()], choices=[])
    valor_atuador = StringField('Valor atuador', validators=[DataRequired()])
    cronometrado = BooleanField('Cronometrado', default=False)
    hora = IntegerField('Hora', validators=[NumberRange(min=00, max=23)])
    minuto = IntegerField('Minuto', validators=[NumberRange(min=00, max=60)])

    def __init__(self, tipo_dispositivo, leaf_id):
        super(RegraSensorForm, self).__init__()
        self.tipo_dispositivo.data = tipo_dispositivo
        self.atuador.choices = Dispositivo.query.filter_by(leaf_id=leaf_id).filter((Dispositivo.tipo=='interruptor') | (Dispositivo.tipo=='potenciometro')).all()
