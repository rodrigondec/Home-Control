from app.models import *
from app import db
from datetime import datetime

db.session.add(RequestLeitura())
db.session.add(RequestEscrita())
db.session.add(AtualizarDispositivo())
db.session.add(AlterarDispositivo())

admin = Administrador('rodrigo', 'rodrigondec@gmail.com', 'rodrigo123')
# admin = Usuario.query.filter_by(id_usuario=1).first()
db.session.add(admin)
#
#
client = Client()
db.session.add(client)
# client = Client.query.filter_by(id_client=1).first()
admin.client = client
#
casa = ModuloPrivado('Casa rod')
# casa = ModuloPrivado.query.filter_by(id_component=1).first()
client.component = casa
#
usuario = Usuario('wesley', 'wereuel@gmail.com', 'wesley123')
# usuario = Usuario.query.filter_by(id_usuario=1).first()
casa.add_usuario(usuario)
casa.add_usuario(admin)


quarto = ModuloPrivado('Quarto de rods')
# quarto = Component.query.filter_by(id_component=2).first()
quarto.add_usuario(admin)
casa.add_component(quarto)
#
leaf = Leaf('Dispositivos do quarto de rods')
# leaf = Component.query.filter_by(id_component=3).first()
quarto.add_component(leaf)


embarcado = Embarcado('0.0.0.0', 'ex:abcd:efgh:ijkl')
# embarcado = Embarcado.query.filter_by(id_embarcado=1).first()
leaf.embarcado = embarcado
#
sensor = Sensor('Temperatura', 13)
# sensor = Dispositivo.query.filter_by(id_dispositivo=1).first()
leaf.add_dispositivo(sensor)
#
interruptor = Interruptor('Lampâda central', 12)
# interruptor = Dispositivo.query.filter_by(id_dispositivo=2).first()
leaf.add_dispositivo(interruptor)
#
potenciometro = Potenciometro('Ventilador', 11)
# potenciometro = Dispositivo.query.filter_by(id_dispositivo=3).first()
leaf.add_dispositivo(potenciometro)
#

monitor = MonitorManual("custom")
# monitor = Monitor.query.filter_by(id_monitor=1).first()
leaf.monitor = monitor
#
regra1 = RegraInterruptor(interruptor, True)
# regra1 = Regra.query.filter_by(id_regra=1).first()
monitor.add_regra(regra1)
#
regra2 = RegraInterruptorCronometrada(interruptor=interruptor, valor=True, hora=datetime.now().hour, minuto=datetime.now().minute)
# regra2 = Regra.query.filter_by(id_regra=2).first()
monitor.add_regra(regra2)
#
regra3 = RegraSensor(sensor=sensor, valor_inicial=10, valor_final=20, regra_atuadora=RegraPotenciometro(potenciometro=potenciometro, valor=0))
# regra3 = Regra.query.filter_by(id_regra=4).first()
monitor.add_regra(regra3)
#
regra4 = RegraSensorCronometrada(sensor=sensor, valor_inicial=10, valor_final=20, regra_atuadora=RegraPotenciometro(potenciometro=potenciometro, valor=3), hora=datetime.now().hour, minuto=datetime.now().minute)
# regra4 = Regra.query.filter_by(id_regra=4).first()
monitor.add_regra(regra4)
#
db.session.commit()
