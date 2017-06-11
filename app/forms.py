from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField, FloatField, HiddenField, SelectMultipleField
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


class AdicionarUsuariosForm(FlaskForm):
    usuarios = SelectMultipleField(u'Usuarios', validators=[DataRequired()], choices=[])

    def __init__(self, usuarios):
        FlaskForm.__init__(self)
        self.usuarios.choices = []
        for usuario in usuarios:
            self.usuarios.choices.append((str(usuario.id_usuario), usuario.nome))


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


class AlterarInterruptorForm(FlaskForm):
    valor = BooleanField(u'Ligado')


class AlterarPotenciometroForm(FlaskForm):
    valor = FloatField(u'Valor', validators=[DataRequired()])


class EmbarcadoForm(FlaskForm):
    ip = StringField(u'Ip', validators=[DataRequired()])
    mac = StringField(u'Mac', validators=[DataRequired()])


class MonitorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    tipo_monitor = SelectField(u'Tipo Monitor',
                                 choices=[('MonitorManual', 'Monitor Manual'), ('MonitorAutomatico', 'Monitor Automático')])


class RegraTipoDispositivoForm(FlaskForm):
    form_name = HiddenField('regra_tipo_dispositivo', default='regra_tipo_dispositivo')
    tipo_dispositivo = SelectField(u'Tipo Dispositivo', validators=[DataRequired()], choices=[('sensor', 'Sensor'), ('interruptor', 'Interruptor'), ('potenciometro', 'Potenciômetro')])


class RegraDispositivoForm(FlaskForm):
    tipo_dispositivo = HiddenField(u'Tipo Dispositivo')
    dispositivo = SelectField(u'Dispositivo', validators=[DataRequired()], choices=[])
    cronometrado = BooleanField(u'Cronometrado', default=False)
    hora = IntegerField(u'Hora', default=0)
    minuto = IntegerField(u'Minuto', default=0)

    def __init__(self, tipo_dispositivo, leaf_id):
        FlaskForm.__init__(self)
        self.tipo_dispositivo.data = tipo_dispositivo
        self.dispositivo.choices = []
        dispositivos = Dispositivo.query.filter_by(leaf_id=leaf_id).filter((Dispositivo.tipo==tipo_dispositivo)).all()
        for dispositivo in dispositivos:
            self.dispositivo.choices.append((str(dispositivo.id_dispositivo), dispositivo.nome))


class RegraInterruptorForm(RegraDispositivoForm):
    form_name = HiddenField('regra_interruptor', default='regra_interruptor')
    valor = BooleanField(u'Ligado')

    def __init__(self, tipo_dispositivo, leaf_id):
        RegraDispositivoForm.__init__(self, tipo_dispositivo, leaf_id)


class RegraPotenciometroForm(RegraDispositivoForm):
    form_name = HiddenField('regra_potenciometro', default='regra_potenciometro')
    valor = FloatField(u'Valor', validators=[DataRequired()])

    def __init__(self, tipo_dispositivo, leaf_id):
        RegraDispositivoForm.__init__(self, tipo_dispositivo, leaf_id)


class RegraSensorForm(RegraDispositivoForm):
    form_name = HiddenField('regra_sensor', default='regra_sensor')
    valor_inicial = FloatField(u'Valor inicial', validators=[DataRequired()])
    valor_final = FloatField(u'Valor final', validators=[DataRequired()])
    atuador = SelectField(u'Atuador', validators=[DataRequired()], choices=[])
    valor_atuador = StringField(u'Valor atuador', validators=[DataRequired()])

    def __init__(self, tipo_dispositivo, leaf_id):
        RegraDispositivoForm.__init__(self, tipo_dispositivo, leaf_id)
        self.atuador.choices = []
        atuadores = Dispositivo.query.filter_by(leaf_id=leaf_id).filter((Dispositivo.tipo=='interruptor') | (Dispositivo.tipo=='potenciometro')).all()
        for atuador in atuadores:
            self.atuador.choices.append((str(atuador.id_dispositivo), atuador.nome))
