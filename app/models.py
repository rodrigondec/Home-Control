from app import db

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

class TemplateStatus(db.Model):
    __abstract__ = True
    status = db.Column(db.String(30))

    def __init__(self, status):
        if self.__class__ is TemplateStatus:
            raise TypeError('abstract class cannot be instantiated')
        self.status = status


class TemplateName(db.Model):
    __abstract__ = True
    nome = db.Column(db.String(80))

    def __init__(self, nome):
        if self.__class__ is TemplateName:
            raise TypeError('abstract class cannot be instantiated')
        self.nome = nome


class Usuario(TemplateName):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(64))

    def __init__(self, nome, email, senha):
        TemplateName.__init__(self, nome)
        self.email = email
        self.senha = senha


class Client(db.Model):
    __tablename__ = 'client'
    id_client = db.Column(db.Integer, primary_key=True)


class Component(TemplateName):
    __tablename__ = 'component'
    id_component = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(15))

    def __init__(self, nome, tipo):
        TemplateName.__init__(self, nome)
        self.tipo = tipo


class Leaf(Component):
    __tablename__ = 'leaf'
    id_leaf = db.Column(db.Integer(), db.ForeignKey("component.id_component"), primary_key=True)
    component = db.relationship("Component")
    embarcado = db.relationship("Embarcado", uselist=False, back_populates="leaf")
    dispositivos = db.relationship("Dispositivo", back_populates="leaf")
    usos = db.relationship("Uso", back_populates="leaf")
    monitor = db.relationship("Monitor", uselist=False, back_populates="leaf")

    def __init__(self, nome):
        Component.__init__(self, nome, self.__tablename__)


class Modulo(Component):
    __tablename__ = 'modulo'
    id_modulo = db.Column(db.Integer(), db.ForeignKey("component.id_component"), primary_key=True)
    component = db.relationship("Component", primaryjoin="and_(Modulo.id_modulo==Component.id_component)")
    components = db.relationship(
        'Component',
        secondary=modulo_component,
        backref=db.backref('modulo', lazy='dynamic')
    )

    def __init__(self, nome):
        Component.__init__(self, nome, self.__tablename__)


class ModuloPrivado(Modulo):
    __tablename__ = 'modulo_privado'
    id_modulo_privado = db.Column(db.Integer(), db.ForeignKey("modulo.id_modulo"), primary_key=True)
    modulo = db.relationship("Modulo", primaryjoin="and_(Modulo.id_modulo==Modulo_privado.id_modulo_privado)")
    usuarios = db.relationship(
        'Usuario',
        secondary=modulo_usuario,
        backref=db.backref('modulos', lazy='dynamic')
    )

    def __init__(self, nome):
        Component.__init__(self, nome, self.__tablename__)


class Embarcado(db.Model):
    __tablename__ = 'embarcado'
    id_embarcado = db.Column(db.Integer, primary_key=True)
    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
    leaf = db.relationship("Leaf", back_populates="embarcado")
    ip = db.Column(db.String(15))
    mac = db.Column(db.String(20))

    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac


class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'
    id_dispositivo = db.Column(db.Integer, primary_key=True)
    porta = db.Column(db.Integer)
    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
    leaf = db.relationship("Leaf", back_populates="dispositivos")
    usos = db.relationship("Uso", back_populates="dispositivo")
    regras = db.relationship("Regra", back_populates="dispositivo")
    tipo = db.Column(db.String(15))

    def __init__(self, porta, tipo):
        self.porta = porta
        self.tipo = tipo


class Sensor(Dispositivo):
    __tablename__ = 'sensor'
    id_sensor = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)

    def __init__(self, porta):
        Dispositivo.__init__(self, porta, self.__tablename__)


class Interruptor(Dispositivo):
    __tablename__ = 'interruptor'
    id_interruptor = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)

    def __init__(self, porta):
        Dispositivo.__init__(self, porta, self.__tablename__)


class Potenciometro(Dispositivo):
    __tablename__ = 'potenciometro'
    id_potenciometro = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)

    def __init__(self, porta):
        Dispositivo.__init__(self, porta, self.__tablename__)


class Uso(TemplateStatus):
    __tablename__ = 'uso'
    id_uso = db.Column(db.Integer, primary_key=True)
    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
    leaf = db.relationship("Leaf", back_populates="usos")
    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = db.relationship("Dispositivo", back_populates="usos")
    comando = db.Column(db.String(30))
    hora = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, status):
        TemplateStatus.__init__(self, status)


class Regra(TemplateStatus):
    __tablename__ = 'regra'
    id_regra = db.Column(db.Integer, primary_key=True)

    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = db.relationship("Dispositivo", back_populates="regras")

    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id_monitor'))
    monitor = db.relationship("Monitor", back_populates="regras")

    def __init__(self, status):
        TemplateStatus.__init__(self, status)


class RegraCronometrada(Regra):
    __tablename__ = 'regra_cronometrada'
    id_regra_cronometrada = db.Column(db.Integer(), db.ForeignKey("regra.id_regra"), primary_key=True)
    hora = db.Column(db.DateTime)

    def __init__(self, hora, status):
        Regra.__init__(self, status)
        self.hora = hora


class Monitor(TemplateName):
    __tablename__ = 'monitor'
    id_monitor = db.Column(db.Integer, primary_key=True)
    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
    leaf = db.relationship("Leaf", back_populates="monitor")

    def __init__(self, nome):
        TemplateName.__init__(self, nome)
