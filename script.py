from app.models import *
from app import db
from datetime import datetime

# admin = Administrador('rodrigo', 'rodrigondec@gmail.com', 'rodrigo123')
# db.session.add(admin)
admin = Administrador.query.filter_by(id_administrador=1).first()
#
# client = Client()
db.session.add(client)
client = Client.query.filter_by(id_client=1).first()
# admin.client = client
#
# casa = ModuloPrivado('Casa rod')
casa = ModuloPrivado.query.filter_by(id_modulo_privado=1).first()
# client.component = casa
#
# usuario = Usuario('wesley', 'wereuelgmail.com', 'wesley123')
usuario = Usuario.query.filter_by(id_usuario=1).first()
# casa.add_usuario(usuario)
# casa.add_usuario(admin)
#
#
# quarto = ModuloPrivado('Quarto de rods')
quarto = ModuloPrivado.query.filter_by(id_modulo_privado=2).first()
# casa.add_component(quarto)

# leaf = Leaf('Dispositivos do quarto de rods')
leaf = Leaf.query.filter_by(id_leaf=3).first()
# quarto.add_component(leaf)
#
# embarcado = Embarcado('0.0.0.0', 'ex:abcd:efgh:ijkl')
embarcado = Embarcado.query.filter_by(id_embarcado=1).first()
# leaf.embarcado = embarcado

# sensor = Sensor(13)
sensor = Sensor.query.filter_by(id_sensor=1).first()
# leaf.add_dispositivo(sensor)

# interruptor = Interruptor(12)
interruptor = Interruptor.query.filter_by(id_interruptor=2).first()
# leaf.add_dispositivo(interruptor)
# leaf.alterar_interruptor(interruptor, True)

# potenciometro = Potenciometro(11)
potenciometro = Potenciometro.query.filter_by(id_potenciometro=3).first()
# leaf.add_dispositivo(potenciometro)
# leaf.alterar_potenciometro(potenciometro, 80.5)

# monitor = MonitorHorario("custom")
monitor = MonitorHorario.query.filter_by(id_monitor_horario=1).first()
# leaf.monitor = monitor

# regra = RegraCronometradaInterruptor(interruptor, True, datetime.now())
regra = RegraCronometradaInterruptor.query.filter_by(id_regra_cronometrada_interruptor=1).first()
# monitor.add_regra(regra)
#
# db.session.commit()
#