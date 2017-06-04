from app import db

# Many-to-many helper tables (for public access, use models only) -----------

modulo_usuario = db.Table(
    'modulo_usuario',
    db.Column(
        'id_modulo_privado',
        db.Integer,
        db.ForeignKey('modulo_privado.id_modulo_privado')
    ),
    db.Column(
        'id_usuario',
        db.Integer,
        db.ForeignKey('usuario.id_usuario')
    )
)

modulo_component = db.Table(
    'modulo_component',
    db.Column(
        'id_modulo',
        db.Integer,
        db.ForeignKey('modulo.id_modulo')
    ),
    db.Column(
        'id_component',
        db.Integer,
        db.ForeignKey('component.id_component'),
        unique=True
    )
)


# Models and their simple relantionships -------------------------------------


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(64))

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_identity': __tablename__,
                       'polymorphic_on': tipo}

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Administrador(Usuario):
    __tablename__ = 'administrador'
    id_administador = db.Column(db.Integer(), db.ForeignKey("usuario.id_usuario", ondelete="CASCADE"), primary_key=True)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id_client'))
    client = db.relationship("Client", uselist=False, backref=db.backref('administrador', lazy='dynamic'))

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, email, senha):
        Usuario.__init__(self, nome, email, senha)


class Client(db.Model):
    __tablename__ = 'client'
    id_client = db.Column(db.Integer, primary_key=True)

    component_id = db.Column(db.Integer, db.ForeignKey('component.id_component'))
    component = db.relationship("Component", uselist=False)


class Component(db.Model):
    __tablename__ = 'component'
    id_component = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, nome):
        if self.__class__ is Dispositivo:
            raise TypeError('abstract class cannot be instantiated')
        self.nome = nome


class Leaf(Component):
    __tablename__ = 'leaf'
    id_leaf = db.Column(db.Integer(), db.ForeignKey("component.id_component", ondelete="CASCADE"), primary_key=True)

    embarcado = db.relationship("Embarcado", uselist=False, back_populates="leaf")

    dispositivos = db.relationship("Dispositivo", back_populates="leaf")

    usos = db.relationship("Uso", back_populates="leaf")

    monitor = db.relationship("Monitor", uselist=False, back_populates="leaf")

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome):
        Component.__init__(self, nome)

    def add_uso(self, uso):
        if uso in self.usos:
            raise Exception("Component duplicado")
        self.usos.append(uso)

    def add_dispositivo(self, dispositivo):
        if dispositivo in self.dispositivos:
            raise Exception("Component duplicado")
        self.dispositivos.append(dispositivo)

    def remove_dispositivo(self, dispositivo):
        self.dispositivos.remove(dispositivo)

    def atualizar_sensor(self, sensor):
        if sensor in self.dispositivos:
            # Mock de acesso ao servidor pegando:
            # self.embarcado.ip < ip do servidor de embarcado
            # sensor.porta < porta do sensor no embarcado
            # request para: 'http://'+self.embarcado.ip+'/sensor/'+sensor.porta
            # retorna um valor
            return_value = 31.5
            sensor.set_valor(return_value)
        else:
            raise Exception("Sensor não achado")

    def atualizar_interruptor(self, interruptor):
        if interruptor in self.dispositivos:
            # Mock de acesso ao servidor pegando:
            # self.embarcado.ip < ip do servidor de embarcado
            # interruptor.porta < porta do sensor no embarcado
            # request para: 'http://'+self.embarcado.ip+'/interruptor/'+interruptor.porta
            # retorna um valor
            return_value = True
            interruptor.set_valor(return_value)
        else:
            raise Exception("Interruptor não achado")

    def atualizar_potenciometro(self, potenciometro):
        if potenciometro in self.dispositivos:
            # Mock de acesso ao servidor pegando:
            # self.embarcado.ip < ip do servidor de embarcado
            # interruptor.porta < porta do sensor no embarcado
            # request para: 'http://'+self.embarcado.ip+'/potenciometro/'+potenciometro.porta
            # retorna um valor
            return_value = 50.5
            potenciometro.set_valor(return_value)
        else:
            raise Exception("Interruptor não achado")

    def alterar_interruptor(self, interruptor, valor):
        if interruptor in self.dispositivos:
            # Mock de acesso ao servidor pegando:
            # self.embarcado.ip < ip do servidor de embarcado
            # interruptor.porta < porta do sensor no embarcado
            # request para: 'http://'+self.embarcado.ip+'/interruptor/'+interruptor.porta+'/'+valor
            self.atualizar_interruptor(interruptor)
            self.add_uso(UsoInterruptor(interruptor, valor))
        else:
            raise Exception("Interruptor não achado")

    def alterar_potenciometro(self, potenciometro, valor):
        if potenciometro in self.dispositivos:
            # Mock de acesso ao servidor pegando:
            # self.embarcado.ip < ip do servidor de embarcado
            # interruptor.porta < porta do sensor no embarcado
            # request para: 'http://'+self.embarcado.ip+'/potenciometro/'+potenciometro.porta+'/'+valor
            self.atualizar_potenciometro(potenciometro)
            self.add_uso(UsoPotenciometro(potenciometro, valor))
        else:
            raise Exception("Interruptor não achado")


class Modulo(Component):
    __tablename__ = 'modulo'
    id_modulo = db.Column(db.Integer(), db.ForeignKey("component.id_component"), primary_key=True)

    components = db.relationship(
        'Component',
        secondary=modulo_component,
        backref=db.backref('component_modulo', lazy='dynamic')
    )

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome):
        Component.__init__(self, nome)

    def add_component(self, component):
        if component in self.components:
            raise Exception("Component duplicado")
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)


class ModuloPrivado(Modulo):
    __tablename__ = 'modulo_privado'
    id_modulo_privado = db.Column(db.Integer(), db.ForeignKey("modulo.id_modulo"), primary_key=True)

    usuarios = db.relationship(
        'Usuario',
        secondary=modulo_usuario,
        backref=db.backref('modulos', lazy='dynamic')
    )

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome):
        Component.__init__(self, nome)

    def add_usuario(self, usuario):
        if usuario in self.usuarios:
            raise Exception("Usuário duplicado")
        self.usuarios.append(usuario)

    def remove_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def add_component(self, component):
        if component in self.components:
            raise Exception("Component duplicado")
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)


class Embarcado(db.Model):
    __tablename__ = 'embarcado'
    id_embarcado = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15))
    mac = db.Column(db.String(20))

    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
    leaf = db.relationship("Leaf", back_populates="embarcado")

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

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, porta):
        if self.__class__ is Dispositivo:
            raise TypeError('abstract class cannot be instantiated')
        self.porta = porta


class Sensor(Dispositivo):
    __tablename__ = 'sensor'
    id_sensor = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, porta):
        Dispositivo.__init__(self, porta)
        self.valor = None

    def set_valor(self, valor):
        if not isinstance(valor, float):
            raise TypeError("Valor precisa ser float")
        self.valor = valor

    def get_valor(self):
        return self.valor


class Interruptor(Dispositivo):
    __tablename__ = 'interruptor'
    id_interruptor = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, porta):
        Dispositivo.__init__(self, porta)
        self.valor = None

    def set_valor(self, valor):
        if not isinstance(valor, bool):
            raise TypeError("Valor precisa ser boolean")
        self.valor = valor

    def get_valor(self):
        return self.valor


class Potenciometro(Dispositivo):
    __tablename__ = 'potenciometro'
    id_potenciometro = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, porta):
        Dispositivo.__init__(self, porta)
        self.valor = None

    def set_valor(self, valor):
        if not isinstance(valor, float):
            raise TypeError("Valor precisa ser float")
        self.valor = valor

    def get_valor(self):
        return self.valor


class Uso(db.Model):
    __tablename__ = 'uso'
    id_uso = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.DateTime, default=db.func.now())

    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
    leaf = db.relationship("Leaf", back_populates="usos")

    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = db.relationship("Dispositivo", back_populates="usos")

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, dispositivo):
        if self.__class__ is Regra:
            raise TypeError('abstract class cannot be instantiated')
        self.dispositivo = dispositivo


class UsoInterruptor(Uso):
    __tablename__ = 'uso_interruptor'
    id_uso_interruptor = db.Column(db.Integer(), db.ForeignKey("uso.id_uso"), primary_key=True)
    valor = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor):
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        Uso.__init__(self, interruptor)
        self.valor = valor


class UsoPotenciometro(Uso):
    __tablename__ = 'uso_potenciometro'
    id_uso_potenciometro = db.Column(db.Integer(), db.ForeignKey("uso.id_uso"), primary_key=True)
    valor = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor):
        if not isinstance(valor, float):
            raise TypeError("Valor não é um boolean")
        Uso.__init__(self, potenciometro)
        self.valor = valor


class Regra(db.Model):
    __tablename__ = 'regra'
    id_regra = db.Column(db.Integer, primary_key=True)

    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = db.relationship("Dispositivo", back_populates="regras")

    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id_monitor'))
    monitor = db.relationship("Monitor", back_populates="regras")

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, dispositivo):
        if self.__class__ is Regra:
            raise TypeError('abstract class cannot be instantiated')
        self.dispositivo = dispositivo


class RegraInterruptor(Regra):
    __tablename__ = 'regra_interruptor'
    id_regra_interruptor = db.Column(db.Integer(), db.ForeignKey("regra.id_regra"), primary_key=True)
    valor = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor):
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        if not isinstance(interruptor, Interruptor):
            raise TypeError("Dispositivo passado não é um Interruptor")
        Regra.__init__(self, interruptor)
        self.valor = valor


class RegraPotenciometro(Regra):
    __tablename__ = 'regra_potenciometro'
    id_regra_potenciometro = db.Column(db.Integer(), db.ForeignKey("regra.id_regra"), primary_key=True)
    valor = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor):
        if not isinstance(valor, float):
            raise TypeError("Valor não é um float")
        if not isinstance(potenciometro, Potenciometro):
            raise TypeError("Dispositivo passado não é um Potenciometro")
        Regra.__init__(self, potenciometro)
        self.valor = valor


class RegraCronometrada(Regra):
    __tablename__ = 'regra_cronometrada'
    id_regra_cronometrada = db.Column(db.Integer(), db.ForeignKey("regra.id_regra"), primary_key=True)
    hora = db.Column(db.DateTime)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, dispositivo, hora):
        if self.__class__ is RegraCronometrada:
            raise TypeError('abstract class cannot be instantiated')
        Regra.__init__(self, dispositivo)
        self.hora = hora


class RegraCronometradaInterruptor(RegraCronometrada):
    __tablename__ = 'regra_cronometrada_interruptor'
    id_regra_cronometrada_interruptor = db.Column(db.Integer(),
                                                  db.ForeignKey("regra_cronometrada.id_regra_cronometrada"),
                                                  primary_key=True)
    valor = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor, hora):
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        if not isinstance(interruptor, Interruptor):
            raise TypeError("Dispositivo passado não é um Interruptor")
        RegraCronometrada.__init__(self, interruptor, hora)
        self.valor = valor


class RegraCronometradaPotenciometro(RegraCronometrada):
    __tablename__ = 'regra_cronometrada_potenciometro'
    id_regra_cronometrada_potenciometro = db.Column(db.Integer(),
                                                    db.ForeignKey("regra_cronometrada.id_regra_cronometrada"),
                                                    primary_key=True)
    valor = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor, hora):
        if not isinstance(valor, float):
            raise TypeError("Valor não é um float")
        if not isinstance(potenciometro, Potenciometro):
            raise TypeError("Dispositivo passado não é um Potenciometro")
        RegraCronometrada.__init__(self, hora)
        self.valor = valor


class Monitor(db.Model):
    __tablename__ = 'monitor'
    id_monitor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))

    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_leaf'))
    leaf = db.relationship("Leaf", back_populates="monitor")

    regras = db.relationship("Regra", back_populates="monitor")

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, nome):
        if self.__class__ is Monitor:
            raise TypeError('abstract class cannot be instantiated')
        self.nome = nome


class MonitorHorario(Monitor):
    __tablename__ = 'monitor_horario'
    id_moitor_horario = db.Column(db.Integer(), db.ForeignKey("monitor.id_monitor"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome):
        Monitor.__init__(self, nome)

    def add_regra(self, regra):
        if regra in self.regras:
            raise Exception("Regra duplicada")
        if not isinstance(regra, RegraCronometrada):
            raise TypeError("Precisa ser uma RegraCronometrada")
        self.regras.append(regra)

    def remove_regra(self, regra):
        self.regras.remove(regra)


class MonitorAutomatico(Monitor):
    __tablename__ = 'monitor_automatico'
    id_moitor_automatico = db.Column(db.Integer(), db.ForeignKey("monitor.id_monitor"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome):
        Monitor.__init__(self, nome)
