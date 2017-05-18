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
        'id_modulo_privado',
        db.Integer,
        db.ForeignKey('modulo_privado.id_modulo_privado')
    )
)

modulo_component = db.Table(
    'modulo_component',
    db.Column(
        'id_component',
        db.Integer,
        db.ForeignKey('component.id_component'),
        unique=True
    ),
    db.Column(
        'id_modulo',
        db.Integer,
        db.ForeignKey('modulo.id_modulo')
    )
)


# Models and their simple relantionships -------------------------------------

class TemplateName(db.Model):
	__abstract__ = True

	nome = db.Column(db.String(80))

	def __init__(self, nome):
		if self.__class__ is TemplateName:
			raise TypeError('abstract class cannot be instantiated')
		self.nome = nome

class Usuario(TemplateName):
	id_usuario = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), unique=True)
	senha = db.Column(db.String(64))

	def __init__(self, nome, email, senha):
		super().__init__(nome)
		self.email = email
		self.senha = senha

class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)

class Component(TemplateName):
	id_component = db.Column(db.Integer, primary_key=True)
	tipo = db.Column(db.String(10))

	def __init__(self, nome, tipo):
		super().__init__(self, nome)
		self.tipo = tipo

class Leaf(db.Model):
	id_leaf = db.Column(db.Integer, primary_key=True)
	component_id = db.Column(db.Integer, db.ForeignKey('component.id_component'))
	component = db.relationship("Component")
	embarcado = db.relationship("Embarcado", uselist=False, back_populates="leaf")
	dispositivos = db.relationship("Dispositivo", back_populates="leaf")
	# children = relationship("Child")
	monitor = db.relationship("Monitor", uselist=False, back_populates="leaf")

class Modulo(db.Model):
	id_modulo = db.Column(db.Integer, primary_key=True)
	component_id = db.Column(db.Integer, db.ForeignKey('component.id_component'))
	component = db.relationship("Component")
	components = db.relationship(
        'Component',
        secondary=modulo_component,
        backref=db.backref('modulo', lazy='dynamic')
    )

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
	ip = db.Column(db.String(15))
	mac = db.Column(db.String(20))

	def __init__(self, ip, mac):
		self.ip = ip
		self.mac = mac

class Dispositivo(db.Model):
	id_dispositivo = db.Column(db.Integer, primary_key=True)
	porta = db.Column(db.Integer)
	leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
	leaf = db.relationship("Leaf", back_populates="dispositivos")
	usos = db.relationship("Uso", back_populates="dispositivo")
	tipo = db.Column(db.String(10))

	def __init__(self, porta, tipo):
		self.porta = porta
		self.tipo = tipo

class Sensor(db.Model):
	id_sensor =  db.Column(db.Integer, primary_key=True)
	dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
	dispositivo = db.relationship("Dispositivo")

class Interruptor(db.Model):
	id_interruptor =  db.Column(db.Integer, primary_key=True)
	dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
	dispositivo = db.relationship("Dispositivo")

class Potenciometro(db.Model):
	id_potenciometro =  db.Column(db.Integer, primary_key=True)
	dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
	dispositivo = db.relationship("Dispositivo")

class Uso(db.Model):
	id_uso = db.Column(db.Integer, primary_key=True)
	dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
	dispositivo = db.relationship("Dispositivo", back_populates="usos")
	comando = db.Column(db.String(30))
	hora = db.Column(db.DateTime, default=db.func.now())

	def __init__(self, comando):
		self.comando = comando

class Monitor(TemplateName):
	id_monitor = db.Column(db.Integer, primary_key=True)
	leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
	leaf = db.relationship("Leaf", back_populates="monitor")

	def __init__(self, nome):
		super().__init__(nome)