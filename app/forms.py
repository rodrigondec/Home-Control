from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField, FloatField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, NumberRange


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
    nome = StringField('Nome', validators=[DataRequired()])
    tipo_component = SelectField('Tipo Componente',
                                 choices=[('Leaf', 'Folha'), ('Modulo', 'Módulo Público'), ('ModuloPrivado', 'Módulo Privado')])
	

class DispositivoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    porta = IntegerField('Porta', validators=[DataRequired()])
    tipo_dispositivo = SelectField('Tipo Dispositivo',
                                 choices=[('Sensor', 'Sensor'), ('Interruptor', 'Interruptor'), ('Potenciometro', 'Potenciômetro')])


class EmbarcadoForm(FlaskForm):
    ip = StringField('Pp', validators=[DataRequired()])
    mac = StringField('Mac', validators=[DataRequired()])


class MonitorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    tipo_monitor = SelectField('Tipo Monitor',
                                 choices=[('MonitorManual', 'Monitor Manual'), ('MonitorAutomatico', 'Monitor Automático')])


class RegraTipoDispositivoForm(FlaskForm):
    form_name = HiddenField('regra_tipo_dispositivo')
    tipo_dispositivo = SelectField('Tipo Dispositivo', validators=[DataRequired()], choices=[('Sensor', 'Sensor'), ('Interruptor', 'Interruptor'), ('Potenciometro', 'Potenciômetro')])


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
