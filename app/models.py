from app import db
from threading import Thread
from datetime import datetime

# Many-to-many helper tables (for public access, use models only) -----------

modulo_usuario = db.Table(
    'modulo_usuario',
    db.Column(
        'id_component',
        db.Integer,
        db.ForeignKey('modulo_privado.id_component')
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
        'id_component_pai',
        db.Integer,
        db.ForeignKey('modulo.id_component')
    ),
    db.Column(
        'id_component_filho',
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
    id_usuario = db.Column(db.Integer(), db.ForeignKey("usuario.id_usuario", ondelete="CASCADE"), primary_key=True)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id_client'))
    client = db.relationship("Client", uselist=False, back_populates='administrador')

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, email, senha):
        Usuario.__init__(self, nome, email, senha)


class Client(db.Model):
    __tablename__ = 'client'
    id_client = db.Column(db.Integer, primary_key=True)

    administrador = db.relationship("Administrador", uselist=False, back_populates="client")

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

    def alteravel_por(self, usuario):
        raise TypeError('abstract method cannot be called')

    def acessivel_por(self, usuario):
        raise TypeError('abstract method cannot be called')


class Leaf(Component):
    __tablename__ = 'leaf'
    id_component = db.Column(db.Integer(),
                             db.ForeignKey("component.id_component", ondelete="CASCADE"), primary_key=True)

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

    def achar_pai_privado(self):
        modulos = Component.query.filter((Component.tipo == 'modulo_privado') | (Component.tipo == 'modulo')).all()
        modulo_atual = self
        while modulo_atual.tipo != 'modulo_privado':
            for modulo in modulos:
                if modulo_atual in modulo.components:
                    # modulos.remove(modulo_atual)
                    modulo_atual = modulo
                    break
        return modulo_atual

    def alteravel_por(self, usuario):
        return self.achar_pai_privado().alteravel_por(usuario)

    def acessivel_por(self, usuario):
        return self.achar_pai_privado().acessivel_por(usuario)


class Modulo(Component):
    __tablename__ = 'modulo'
    id_component = db.Column(db.Integer(), db.ForeignKey("component.id_component"), primary_key=True)

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

    def achar_pai_privado(self):
        modulos = Component.query.filter((Component.tipo == 'modulo_privado') | (Component.tipo == 'modulo')).all()
        modulo_atual = self
        while modulo_atual.tipo != 'modulo_privado':
            for modulo in modulos:
                if modulo_atual in modulo.components:
                    modulos.remove(modulo_atual)
                    modulo_atual = modulo
                    break
        return modulo_atual

    def alteravel_por(self, usuario):
        return self.achar_pai_privado().alteravel_por(usuario)

    def acessivel_por(self, usuario):
        return self.achar_pai_privado().acessivel_por(usuario)


class ModuloPrivado(Modulo):
    __tablename__ = 'modulo_privado'
    id_component = db.Column(db.Integer(), db.ForeignKey("modulo.id_component"), primary_key=True)

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

    def alteravel_por(self, usuario):
        client = Client.query.filter_by(id_client=1).first()
        if self == client.component and usuario.tipo != 'administrador':
            return False
        return self.acessivel_por(usuario)

    def acessivel_por(self, usuario):
        if usuario in self.usuarios:
            return True
        return False


class Embarcado(db.Model):
    __tablename__ = 'embarcado'
    id_embarcado = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15))
    mac = db.Column(db.String(20))

    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_component'))
    leaf = db.relationship("Leaf", back_populates="embarcado")

    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac


class Dispositivo(db.Model):
    __tablename__ = 'dispositivo'
    id_dispositivo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    porta = db.Column(db.Integer)

    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_component'))
    leaf = db.relationship("Leaf", back_populates="dispositivos")

    usos = db.relationship("Uso", back_populates="dispositivo")

    regras = db.relationship("Regra", back_populates="dispositivo")

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, nome, porta):
        if self.__class__ is Dispositivo:
            raise TypeError('abstract class cannot be instantiated')
        self.nome = nome
        self.porta = porta

    def get_valor(self):
        raise TypeError('abstract method cannot be called')


class Sensor(Dispositivo):
    __tablename__ = 'sensor'
    id_dispositivo = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)
    valor = db.Column(db.Float())

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, porta):
        Dispositivo.__init__(self, nome, porta)

    def get_valor(self):
        return self.valor


class Interruptor(Dispositivo):
    __tablename__ = 'interruptor'
    id_dispositivo = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)
    valor = db.Column(db.Boolean())

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, porta):
        Dispositivo.__init__(self, nome, porta)

    def get_valor(self):
        return self.valor


class Potenciometro(Dispositivo):
    __tablename__ = 'potenciometro'
    id_dispositivo = db.Column(db.Integer(), db.ForeignKey("dispositivo.id_dispositivo"), primary_key=True)
    valor = db.Column(db.Float())

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, porta):
        Dispositivo.__init__(self, nome, porta)

    def get_valor(self):
        return self.valor


class Uso(db.Model):
    __tablename__ = 'uso'
    id_uso = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.DateTime, default=db.func.now())

    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_component'))
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
    id_uso = db.Column(db.Integer(), db.ForeignKey("uso.id_uso"), primary_key=True)
    valor = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor):
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        Uso.__init__(self, interruptor)
        self.valor = valor


class UsoPotenciometro(Uso):
    __tablename__ = 'uso_potenciometro'
    id_uso = db.Column(db.Integer(), db.ForeignKey("uso.id_uso"), primary_key=True)
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

    def avaliar_regra(self):
        raise TypeError('abstract method cannot be called')

    def execute(self):
        raise TypeError('abstract method cannot be called')


class RegraInterruptor(Regra):
    __tablename__ = 'regra_interruptor'
    id_regra = db.Column(db.Integer(), db.ForeignKey("regra.id_regra"), primary_key=True)
    valor = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor):
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        if not isinstance(interruptor, Interruptor):
            raise TypeError("Dispositivo passado não é um Interruptor")
        Regra.__init__(self, interruptor)
        self.valor = valor

    def avaliar_regra(self):
        return self.dispositivo.get_valor() != self.valor

    def execute(self):
        raise Exception('not implemented')


class RegraPotenciometro(Regra):
    __tablename__ = 'regra_potenciometro'
    id_regra = db.Column(db.Integer(), db.ForeignKey("regra.id_regra"), primary_key=True)
    valor = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor):
        if isinstance(valor, int):
            valor = float(valor)
        if not isinstance(valor, float):
            raise TypeError("Valor não é um float")
        if not isinstance(potenciometro, Potenciometro):
            raise TypeError("Dispositivo passado não é um Potenciometro")
        Regra.__init__(self, potenciometro)
        self.valor = valor

    def avaliar_regra(self):
        return self.dispositivo.get_valor() != self.valor

    def execute(self):
        raise Exception('not implemented')


class RegraSensor(Regra):
    __tablename__ = 'regra_sensor'
    id_regra = db.Column(db.Integer(), db.ForeignKey("regra.id_regra"), primary_key=True)
    valor_inicial = db.Column(db.Float)
    valor_final = db.Column(db.Float)

    regra_atuadora_id = db.Column(db.Integer, db.ForeignKey('regra.id_regra'))
    regra_atuadora = db.relationship("Regra", foreign_keys=[regra_atuadora_id])

    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'inherit_condition': (id_regra==Regra.id_regra)
    }

    def __init__(self, sensor, valor_inicial, valor_final, regra_atuadora):
        if isinstance(valor_inicial, int):
            valor_inicial = float(valor_final)
        if isinstance(valor_final, int):
            valor_final = float(valor_final)
        if not isinstance(valor_inicial, float) or not isinstance(valor_final, float):
            raise TypeError("Valor não é um float")
        if not isinstance(sensor, Sensor):
            raise TypeError("Dispositivo passado não é um Sensor")
        if not isinstance(regra_atuadora, RegraPotenciometro) and not isinstance(regra_atuadora, RegraInterruptor):
            raise TypeError("Regra atuadora não é valida")
        Regra.__init__(self, sensor)
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final
        self.regra_atuadora = regra_atuadora

    def avaliar_regra(self):
        raise Exception('not implemented')

    def execute(self):
        raise Exception('not implemented')


    minuto = db.Column(db.Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, dispositivo, hora, minuto):
        if self.__class__ is RegraCronometrada:
            raise TypeError('abstract class cannot be instantiated')
        Regra.__init__(self, dispositivo)
        self.hora = hora
        self.minuto = minuto


class RegraCronometradaInterruptor(RegraCronometrada):
    __tablename__ = 'regra_cronometrada_interruptor'
    id_regra = db.Column(db.Integer(),
                         db.ForeignKey("regra_cronometrada.id_regra"),
                         primary_key=True)
    valor = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor, hora, minuto):
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        if not isinstance(interruptor, Interruptor):
            raise TypeError("Dispositivo passado não é um Interruptor")
        RegraCronometrada.__init__(self, interruptor, hora, minuto)
        self.valor = valor

    def avaliar_regra(self):
        return self.hora == datetime.now().hour and self.minuto == datetime.now().minute and self.dispositivo.get_valor() != self.valor


class RegraCronometradaPotenciometro(RegraCronometrada):
    __tablename__ = 'regra_cronometrada_potenciometro'
    id_regra = db.Column(db.Integer(),
                         db.ForeignKey("regra_cronometrada.id_regra"),
                         primary_key=True)
    valor = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor, hora, minuto):
        if not isinstance(valor, float):
            raise TypeError("Valor não é um float")
        if not isinstance(potenciometro, Potenciometro):
            raise TypeError("Dispositivo passado não é um Potenciometro")
        RegraCronometrada.__init__(self, potenciometro, hora, minuto)
        self.valor = valor

    def avaliar_regra(self):
        return self.hora == datetime.now().hour and self.minuto == datetime.now().minute and self.dispositivo.get_valor() != self.valor


class Monitor(db.Model, Thread):
    __tablename__ = 'monitor'
    id_monitor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))

    leaf_id = db.Column(db.Integer, db.ForeignKey('leaf.id_component'))
    leaf = db.relationship("Leaf", back_populates="monitor")

    regras = db.relationship("Regra", back_populates="monitor")

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, nome):
        if self.__class__ is Monitor:
            raise TypeError('abstract class cannot be instantiated')
        Thread.__init__(self)
        self.nome = nome

    def add_regra(self, regra):
        if regra in self.regras:
            raise Exception("Regra duplicada")
        self.regras.append(regra)

    def remove_regra(self, regra):
        self.regras.remove(regra)

    def before_run(self):
        raise TypeError('abstract method cannot be called')

    def run(self):
        raise TypeError('abstract method cannot be called')

    def verificar_regras(self):
        raise TypeError('abstract method cannot be called')

    def executar_comando(self, regra):
        raise TypeError('abstract method cannot be called')

    def after_run(self):
        raise TypeError('abstract method cannot be called')


class MonitorManual(Monitor):
    __tablename__ = 'monitor_manual'
    id_monitor = db.Column(db.Integer(), db.ForeignKey("monitor.id_monitor"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome):
        Monitor.__init__(self, nome)


class MonitorAutomatico(Monitor):
    __tablename__ = 'monitor_automatico'
    id_monitor = db.Column(db.Integer(), db.ForeignKey("monitor.id_monitor"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome):
        Monitor.__init__(self, nome)


class Command(db.Model):
    __tablename__ = 'command'
    id_command = db.Column(db.Integer, primary_key=True)

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self):
        if self.__class__ is Command:
            raise TypeError('abstract class cannot be instantiated')

    def execute(self):
        raise TypeError('abstract method cannot be called')

    def after_execute(self):
        raise TypeError('abstract method cannot be called')


class RequestLeitura(Command):
    __tablename__ = 'request_leitura'
    id_command = db.Column(db.Integer(), db.ForeignKey("command.id_command"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self):
        Command.__init__(self)

    def before_execute(self, ip, porta):
        self.ip = ip
        self.porta = porta

    def execute(self):
        self.after_execute()

        return 1.0

    def after_execute(self):
        pass


class RequestEscrita(Command):
    __tablename__ = 'request_escrita'
    id_command = db.Column(db.Integer(), db.ForeignKey("command.id_command"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self):
        Command.__init__(self)

    def before_execute(self, ip, porta, valor):
        self.ip = ip
        self.porta = porta
        self.valor = valor

    def execute(self):
        self.after_execute()
        pass

    def after_execute(self):
        pass


class AtualizarDispositivo(Command):
    __tablename__ = 'atualizar_dispositivo'
    id_command = db.Column(db.Integer(), db.ForeignKey("command.id_command"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self):
        Command.__init__(self)

    def before_execute(self, embarcado, dispositivo):
        if not isinstance(embarcado, Embarcado):
            raise TypeError("parâmetro 1 precisa ser do tipo Embarcado")
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("parâmetro 2 precisa ser do tipo Dispositivo")
        self.embarcado = embarcado
        self.dispositivo = dispositivo

    def execute(self):
        request = RequestLeitura()
        request.before_execute(self.embarcado.ip, self.dispositivo.porta)
        self.dispositivo.valor = request.execute()
        db.commit()
        self.after_execute()

    def after_execute(self):
        pass


class AlterarDispositivo(Command):
    __tablename__ = 'alterar_dispositivo'
    id_command = db.Column(db.Integer(), db.ForeignKey("command.id_command"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self):
        Command.__init__(self)

    def before_execute(self, embarcado, dispositivo, valor):
        if not isinstance(embarcado, Embarcado):
            raise TypeError("parâmetro 1 precisa ser do tipo Embarcado")
        if not isinstance(dispositivo, Potenciometro) and not isinstance(dispositivo, Interruptor):
            raise TypeError("parâmetro 2 precisa ser do tipo Potenciometro ou Interruptor")
        self.embarcado = embarcado
        self.dispositivo = dispositivo
        self.valor = valor

    def execute(self):
        request = RequestEscrita()
        request.before_execute(self.embarcado.ip, self.dispositivo.porta, self.valor)
        request.execute()
        self.dispositivo.valor = self.after_execute()
        db.commit()

    def after_execute(self):
        request = RequestLeitura()
        request.before_execute(self.embarcado.ip, self.dispositivo.porta)
        return request.execute()
