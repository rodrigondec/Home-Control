from app.models import *
from app import db
from datetime import datetime

db.session.add(RequestLeitura())
db.session.add(RequestEscrita())
db.session.add(AtualizarDispositivo())
db.session.add(AlterarDispositivo())

admin = Administrador('rodrigo', 'rodrigondec@gmail.com', 'rodrigo123')
db.session.add(admin)
# admin = Administrador.query.filter_by(id_usuario=1).first()

client = Client()
# db.session.add(client)
# client = Client.query.filter_by(id_client=1).first()
admin.client = client

casa = ModuloPrivado('Casa rod')
# casa = ModuloPrivado.query.filter_by(id_component=1).first()
client.component = casa

usuario = Usuario('wesley', 'wereuel@gmail.com', 'wesley123')
# usuario = Usuario.query.filter_by(id_usuario=1).first()
casa.add_usuario(usuario)
casa.add_usuario(admin)


quarto = ModuloPrivado('Quarto de rods')
# quarto = ModuloPrivado.query.filter_by(id_component=2).first()
quarto.add_usuario(admin)
casa.add_component(quarto)
#
leaf = Leaf('Dispositivos do quarto de rods')
# leaf = Leaf.query.filter_by(id_component=3).first()
quarto.add_component(leaf)

embarcado = Embarcado('0.0.0.0', 'ex:abcd:efgh:ijkl')
# embarcado = Embarcado.query.filter_by(id_embarcado=1).first()
leaf.embarcado = embarcado
#
sensor = Sensor('Temperatura', 13)
# sensor = Sensor.query.filter_by(id_dispositivo=1).first()
leaf.add_dispositivo(sensor)
#
interruptor = Interruptor('Lampâda central', 12)
# interruptor = Interruptor.query.filter_by(id_dispositivo=2).first()
leaf.add_dispositivo(interruptor)
#
potenciometro = Potenciometro('Ventilador', 11)
# potenciometro = Potenciometro.query.filter_by(id_dispositivo=3).first()
leaf.add_dispositivo(potenciometro)
#
monitor = MonitorHorario("custom")
# monitor = MonitorHorario.query.filter_by(id_monitor=1).first()
leaf.monitor = monitor
#
regra = RegraCronometradaInterruptor(interruptor, True, datetime.now().hour, datetime.now().minute)
# regra = RegraCronometradaInterruptor.query.filter_by(id_regra=1).first()
monitor.add_regra(regra)

regra2 = RegraInterruptor(interruptor, True)
# regra2 = RegraCronometradaInterruptor.query.filter_by(id_regra=2).first()
monitor.add_regra(regra2)


db.session.commit()
