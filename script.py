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
temperatura = Sensor('Temperatura', 13)
# temperatura = Dispositivo.query.filter_by(id_dispositivo=1).first()
leaf.add_dispositivo(temperatura)
#
lampada = Interruptor('Lampâda central', 12)
# lampada = Dispositivo.query.filter_by(id_dispositivo=2).first()
leaf.add_dispositivo(lampada)

ar = Interruptor('Ar-condicionado', 14)
# ar = Dispositivo.query.filter_by(id_dispositivo=3).first()
leaf.add_dispositivo(ar)

porta = Interruptor('Porta', 15)
# porta = Dispositivo.query.filter_by(id_dispositivo=4).first()
leaf.add_dispositivo(porta)
#
ventilador = Potenciometro('Ventilador', 11)
# ventilador = Dispositivo.query.filter_by(id_dispositivo=5).first()
leaf.add_dispositivo(ventilador)
#

monitor = Monitor("custom")
# monitor = Monitor.query.filter_by(id_monitor=1).first()
leaf.monitor = monitor
#
regra1 = Regra(monitor=monitor, condicao=CondicaoInterruptor(ar, True), atuador=AtuadorInterruptor(porta, False))
# regra1 = Regra.query.filter_by(id_regra=1).first()
#
regra2 = Regra(monitor=monitor, condicao=CondicaoInterruptor(ar, True), atuador=AtuadorPotenciometro(ventilador, 0))
# regra2 = Regra.query.filter_by(id_regra=2).first()
#
regra3 = Regra(monitor=monitor, condicao=CondicaoInterruptorCronometrada(lampada, False, hora=18, minuto=00), atuador=AtuadorInterruptor(lampada, True))
# regra3 = Regra.query.filter_by(id_regra=5).first()
#
regra4 = Regra(monitor=monitor, condicao=CondicaoSensor(temperatura, 23, 40), atuador=AtuadorInterruptor(ar, True))
# regra4 = Regra.query.filter_by(id_regra=6).first()
#
db.session.commit()
