from app.models import *
from app import db

# client = Client()
# db.session.add(client)
client = Client.query.filter_by(id_client=1).first()

# casa = ModuloPrivado('Casa rod')
# db.session.add(casa)
casa = ModuloPrivado.query.filter_by(id_modulo_privado=1).first()
# client.component = casa

# usuario = Usuario('rodrigo', 'rodrigondec@gmail.com', 'rodrigo123')
# db.session.add(usuario)
usuario = Usuario.query.filter_by(id_usuario=1).first()
# casa.add_usuario(usuario)

# quarto = ModuloPrivado('Quarto de rods')
# db.session.add(quarto)
quarto = ModuloPrivado.query.filter_by(id_modulo_privado=2).first()
# casa.add_component(quarto)

# leaf = Leaf('Dispositivos do quarto de rods')
# db.session.add(leaf)
leaf = Leaf.query.filter_by(id_leaf=3).first()
# quarto.add_component(leaf)

# embarcado = Embarcado('0.0.0.0', 'ex:abcd:efgh:ijkl')
# db.session.add(embarcado)
embarcado = Embarcado.query.filter_by(id_embarcado=1).first()
# leaf.embarcado = embarcado

# sensor = Sensor(13)
# db.session.add(sensor)
sensor = Sensor.query.filter_by(id_sensor=1).first()
# leaf.add_dispositivo(sensor)

# interruptor = Interruptor(12)
# db.session.add(interruptor)
interruptor = Interruptor.query.filter_by(id_interruptor=1).first()
# leaf.add_dispositivo(interruptor)

# @TODO adicionar uso
# @TODO adicionar regra
# @TODO adicionar monitor

db.session.commit()
