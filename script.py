from app.models import *
from app import db

# obj = Usuario('rodrigo', 'rodrigondec@gmail.com', 'rodrigo123')
# obj2 = Sensor(13)
# obj3 = ModuloPrivado('quarto')
# obj4 = Modulo('jardim')

# print(obj.tipo)
# db.session.add(obj)
# db.session.add(obj2)
# db.session.add(obj3)
# db.session.add(obj4)

# obj = Client()
# obj1 = ModuloPrivado('Casa rod')
# db.session.add(obj)
# db.session.add(obj1)
# obj.component = obj1

# client = Client.query.filter_by(id_client=1).first()
# modulo = ModuloPrivado.query.filter_by(id_modulo_privado=3).first()
# quarto = ModuloPrivado.query.filter_by(id_modulo_privado=1).first()
# client.component = modulo.component
# modulo.add_component(quarto.component)
# leaf = Leaf('dispositivos quarto')
# db.session.add(leaf)
# db.session.commit()
# quarto.modulo.add_component(leaf.component)

# leaf = Leaf.query.filter_by(id_leaf=6).first()
# db.session.delete(leaf)

db.session.commit()