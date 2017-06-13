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


class RegraCondicaoAtuadorForm(FlaskForm):
    form_name = HiddenField('regra_tipo_dispositivo', default='regra_condicao_atuador')
    dispositivo_condicao = SelectField(u'Dispositivo Condição', validators=[DataRequired()], choices=[])
    dispositivo_atuador = SelectField(u'Dispositivo Atuador', validators=[DataRequired()], choices=[])

    def __init__(self, leaf_id):
        FlaskForm.__init__(self)
        self.dispositivo_condicao.choices = []
        dispositivos = Dispositivo.query.filter_by(leaf_id=leaf_id).all()
        for dispositivo in dispositivos:
            self.dispositivo_condicao.choices.append((str(dispositivo.id_dispositivo), dispositivo.nome))

        self.dispositivo_atuador.choices = []
        atuadores = Dispositivo.query.filter_by(leaf_id=leaf_id).filter((Dispositivo.tipo == 'potenciometro') | (Dispositivo.tipo == 'interruptor')).all()
        for atuador in atuadores:
            self.dispositivo_atuador.choices.append((str(atuador.id_dispositivo), atuador.nome))


class RegraDispositivoDispositivoForm(FlaskForm):
    form_name = HiddenField('regra_tipo_dispositivo', default='regra_valores')
    id_dispositivo_condicao = HiddenField(u'Dispositivo Condicao')
    tipo_dispositivo_condicao = HiddenField(u'Tipo Dispositivo Condicao')
    id_dispositivo_atuador = HiddenField(u'Dispositivo Atuador')
    tipo_dispositivo_atuador = HiddenField(u'Tipo Dispositivo Atuador')
    cronometrado = BooleanField(u'Cronometrado', default=False)
    hora = IntegerField(u'Hora', default=0)
    minuto = IntegerField(u'Minuto', default=0)

    def __init__(self, dispositivo_condicao, dispositivo_atuador):
        FlaskForm.__init__(self)
        self.id_dispositivo_condicao.data = dispositivo_condicao.id_dispositivo
        self.tipo_dispositivo_condicao = dispositivo_condicao.tipo
        self.id_dispositivo_atuador.data = dispositivo_atuador.id_dispositivo
        self.tipo_dispositivo_atuador = dispositivo_atuador.tipo


class RegraInterruptorInterruptorForm(RegraDispositivoDispositivoForm):
    valor_condicao = BooleanField(u'Valor Condição')
    valor_atuador = BooleanField(u'Valor Atuador')

    def __init__(self, dispositivo_condicao, dispositivo_atuador):
        RegraDispositivoDispositivoForm.__init__(self, dispositivo_condicao, dispositivo_atuador)


class RegraInterruptorPotenciometroForm(RegraDispositivoDispositivoForm):
    valor_condicao = BooleanField(u'Valor Condição')
    valor_atuador = FloatField(u'Valor Atuador')

    def __init__(self, dispositivo_condicao, dispositivo_atuador):
        RegraDispositivoDispositivoForm.__init__(self, dispositivo_condicao, dispositivo_atuador)


class RegraPotenciometroInterruptorForm(RegraDispositivoDispositivoForm):
    valor_inicial_condicao = FloatField(u'Valor Inicial Condição')
    valor_final_condicao = FloatField(u'Valor Final Condição')
    valor_atuador = BooleanField(u'Valor Atuador')

    def __init__(self, dispositivo_condicao, dispositivo_atuador):
        RegraDispositivoDispositivoForm.__init__(self, dispositivo_condicao, dispositivo_atuador)


class RegraPotenciometroPotenciometroForm(RegraDispositivoDispositivoForm):
    valor_inicial_condicao = FloatField(u'Valor Inicial Condição')
    valor_final_condicao = FloatField(u'Valor Final Condição')
    valor_atuador = FloatField(u'Valor Atuador')

    def __init__(self, dispositivo_condicao, dispositivo_atuador):
        RegraDispositivoDispositivoForm.__init__(self, dispositivo_condicao, dispositivo_atuador)


class RegraSensorInterruptorForm(RegraDispositivoDispositivoForm):
    valor_inicial_condicao = FloatField(u'Valor Inicial Condição')
    valor_final_condicao = FloatField(u'Valor Final Condição')
    valor_atuador = BooleanField(u'Valor Atuador')

    def __init__(self, dispositivo_condicao, dispositivo_atuador):
        RegraDispositivoDispositivoForm.__init__(self, dispositivo_condicao, dispositivo_atuador)


class RegraSensorPotenciometroForm(RegraDispositivoDispositivoForm):
    valor_inicial_condicao = FloatField(u'Valor Inicial Condição')
    valor_final_condicao = FloatField(u'Valor Final Condição')
    valor_atuador = FloatField(u'Valor Atuador')

    def __init__(self, dispositivo_condicao, dispositivo_atuador):
        RegraDispositivoDispositivoForm.__init__(self, dispositivo_condicao, dispositivo_atuador)
