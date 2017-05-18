from app.models import *
from app import db

obj = Usuario('rodrigo', 'rodrigondec@gmail.com', 'rodrigo123')
obj2 = Sensor(13)
obj3 = ModuloPrivado('quarto')
obj4 = Modulo('jardim')

# print(obj.tipo)
db.session.add(obj)
db.session.add(obj2)
db.session.add(obj3)
db.session.add(obj4)
db.session.commit()