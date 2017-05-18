from app import db
from sqlalchemy.ext.declarative import declared_attr


# Many-to-many helper tables (for public access, use models only) -----------

modulo_usuario = db.Table(
    'modulo_usuario',
    db.Column(
        'id_usuario',
        db.Integer,
        db.ForeignKey('usuario.id_usuario')
    ),
    db.Column(
        'id_modulo',
        db.Integer,
        db.ForeignKey('modulo_privado.id_modulo_privado')
    )
)

# modulo_component = db.Table(
#     'modulo_component',
#     db.Column(
#         'id_modulo',
#         db.Integer,
#         db.ForeignKey('modulo.id_component')
#     ),
#     db.Column(
#         'id_component',
#         db.Integer,
#         db.ForeignKey('component.id_component')
#     )
# )

# leaf_component = db.Table(
#     'leaf_component',
#     db.Column(
#         'id_leaf',
#         db.Integer,
#         db.ForeignKey('leaf.id_leaf'),
#         unique=True
#     ),
#     db.Column(
#         'id_component',
#         db.Integer,
#         db.ForeignKey('component.id_component'),
#         unique=True
#     )
# )


# Models and their simple relantionships -------------------------------------

class TemplateName(db.Model):
    __abstract__ = True

    nome = db.Column(db.String(80))

class Usuario(TemplateName):
    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(64))

class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)

class Component(TemplateName):
	id_component = db.Column(db.Integer, primary_key=True)
	tipo = db.Column(db.String(10))
	# modulo_id = db.Column(db.Integer, db.ForeignKey('modulo.id_modulo'))
	# @declared_attr
	# def modulo_id(cls):
	# 	return db.Column(db.Integer, db.ForeignKey('modulo.id_modulo'))

class Leaf(Component):
	id_leaf = db.Column(db.Integer, primary_key=True)
	component_id = db.Column(db.Integer, db.ForeignKey('component.id_component'))
	component = db.relationship("Component")
	embarcado = db.relationship("Embarcado", uselist=False, back_populates="leaf")
	dispositivos = db.relationship("Dispositivo", back_populates="leaf")
	monitor = db.relationship("Monitor", uselist=False, back_populates="leaf")

class Modulo(Component):
	id_modulo = db.Column(db.Integer, primary_key=True)
	component_id = db.Column(db.Integer, db.ForeignKey('component.id_component'))
	component = db.relationship("Component")
	components = db.relationship("Component", back_populates="modulo")
	

	# @declared_attr
	# def id_modulo(cls):
	# 	return db.Column(db.Integer(), db.ForeignKey("component.id_component"), primary_key=True)
	# @declared_attr
	# def modulos(cls):
	# 	return db.relationship("Component", back_populates="modulo")

# class ModuloPublico(Modulo):
# 	id_modulo_publico =  db.Column(db.Integer(), db.ForeignKey("modulo.id_modulo"), primary_key=True)

class ModuloPrivado(Modulo):
	id_modulo_privado =  db.Column(db.Integer(), db.ForeignKey("modulo.id_modulo"), primary_key=True)
	usuarios = db.relationship(
        'Usuario',
        secondary=modulo_usuario,
        backref=db.backref('modulos', lazy='dynamic')
    )

class Embarcado(db.Model):
	id_embarcado = db.Column(db.Integer, primary_key=True)
	leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
	leaf = db.relationship("Leaf", back_populates="embarcado")

class Dispositivo(db.Model):
	id_dispositivo = db.Column(db.Integer, primary_key=True)
	leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
	usos = db.relationship("Uso", back_populates="dispositivo")
	tipo = db.Column(db.String(10))

class Sensor(Dispositivo):
	id_sensor =  db.Column(db.Integer, primary_key=True)
	dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
	dispositivo = db.relationship("Dispositivo")

class Interruptor(Dispositivo):
	id_interruptor =  db.Column(db.Integer, primary_key=True)
	dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
	dispositivo = db.relationship("Dispositivo")

class Potenciometro(Dispositivo):
	id_potenciometro =  db.Column(db.Integer, primary_key=True)
	dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
	dispositivo = db.relationship("Dispositivo")

class Uso(db.Model):
	id_uso = db.Column(db.Integer, primary_key=True)
	dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
	comando = db.Column(db.String(30))
	hora = db.Column(db.DateTime, default=db.func.now())

class Monitor(TemplateName):
	id_monitor = db.Column(db.Integer, primary_key=True)
	leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
	leaf = db.relationship("Leaf", back_populates="monitor")


# class Base(db.Model):
#     __abstract__ = True

#     disabled = db.Column(db.Boolean, default=0)
#     inserted_since = db.Column(db.DateTime, default=db.func.now())
#     @declared_attr
#     def inserted_by(cls):
#         return db.Column(db.Integer, db.ForeignKey('user.id_user'))
#     # inserted_by = db.Column(db.Integer, db.ForeignKey('user.id_user'))
#     last_updated_since = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
#     @declared_attr
#     def last_updated_by(cls):
#         return db.Column(db.Integer, db.ForeignKey('user.id_user'))