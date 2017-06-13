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

    def achar_pai(self):
        raise TypeError('abstract method cannot be called')

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

    def achar_pai(self):
        modulos = Component.query.filter((Component.tipo == 'modulo_privado') | (Component.tipo == 'modulo')).all()
        for modulo in modulos:
            if self in modulo.components:
                return modulo
        return self

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

    def achar_pai(self):
        modulos = Component.query.filter((Component.tipo == 'modulo_privado') | (Component.tipo == 'modulo')).all()
        for modulo in modulos:
            if self in modulo.components:
                return modulo
        return self

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

    def achar_pai(self):
        modulos = Component.query.filter((Component.tipo == 'modulo_privado') | (Component.tipo == 'modulo')).all()
        for modulo in modulos:
            if self in modulo.components:
                return modulo
        return self

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

    atuadores = db.relationship("Atuador", back_populates="dispositivo")

    condicoes = db.relationship("Condicao", back_populates="dispositivo")

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

    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id_monitor'))
    monitor = db.relationship("Monitor", back_populates="regras")

    condicao = db.relationship("Condicao", uselist=False, back_populates="regra")

    atuador = db.relationship("Atuador", uselist=False, back_populates="regra")

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, monitor, condicao, atuador):
        if not isinstance(monitor, Monitor):
            raise TypeError('monitor não é do tipo Monitor')
        if not isinstance(condicao, Condicao):
            raise TypeError('condicao não é do tipo Condicao')
        if not isinstance(atuador, Atuador):
            raise TypeError('atuador não é do tipo Atuador')
        self.condicao = condicao
        self.atuador = atuador
        monitor.add_regra(self)


    def avaliar_regra(self):
        raise Exception('not implemented')

    def execute(self):
        raise Exception('not implemented')


class Atuador(db.Model):
    __tablename__ = 'atuador'
    id_atuador = db.Column(db.Integer, primary_key=True)

    regra_id = db.Column(db.Integer, db.ForeignKey('regra.id_regra'))
    regra = db.relationship("Regra", back_populates="atuador")

    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = db.relationship("Dispositivo", back_populates="atuadores")

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, dispositivo):
        if self.__class__ is Atuador:
            raise TypeError('abstract class cannot be instantiated')
        self.dispositivo = dispositivo

    def execute(self):
        raise TypeError('abstract method cannot be called')


class AtuadorInterruptor(Atuador):
    __tablename__ = 'atuador_interruptor'
    id_atuador = db.Column(db.Integer(), db.ForeignKey("atuador.id_atuador"), primary_key=True)
    valor = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor):
        if isinstance(valor, int) or isinstance(valor, float) or isinstance(valor, str):
            valor = bool(valor)
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        if not isinstance(interruptor, Interruptor):
            raise TypeError("Dispositivo passado não é um Interruptor")
        Atuador.__init__(self, interruptor)
        self.valor = valor

    def execute(self):
        raise Exception('not implemented')


class AtuadorPotenciometro(Atuador):
    __tablename__ = 'atuador_potenciometro'
    id_atuador = db.Column(db.Integer(), db.ForeignKey("atuador.id_atuador"), primary_key=True)
    valor = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor):
        if isinstance(valor, int) or isinstance(valor, str):
            valor = float(valor)
        if not isinstance(valor, float):
            raise TypeError("Valor não é um float")
        if not isinstance(potenciometro, Potenciometro):
            raise TypeError("Dispositivo passado não é um Interruptor")
        Atuador.__init__(self, potenciometro)
        self.valor = valor

    def execute(self):
        raise Exception('not implemented')


class Condicao(db.Model):
    __tablename__ = 'condicao'
    id_condicao = db.Column(db.Integer, primary_key=True)

    regra_id = db.Column(db.Integer, db.ForeignKey('regra.id_regra'))
    regra = db.relationship("Regra", back_populates="condicao")

    dispositivo_id = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = db.relationship("Dispositivo", back_populates="condicoes")

    tipo = db.Column(db.String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, dispositivo):
        if self.__class__ is Condicao:
            raise TypeError('abstract class cannot be instantiated')
        self.dispositivo = dispositivo

    def avaliar_condicao(self):
        raise TypeError('abstract method cannot be called')


class CondicaoInterruptor(Condicao):
    __tablename__ = 'condicao_interruptor'
    id_condicao = db.Column(db.Integer(), db.ForeignKey("condicao.id_condicao"), primary_key=True)
    valor = db.Column(db.Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor):
        if isinstance(valor, int) or isinstance(valor, float) or isinstance(valor, str):
            valor = bool(valor)
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        if not isinstance(interruptor, Interruptor):
            raise TypeError("Dispositivo passado não é um Interruptor")
        Condicao.__init__(self, interruptor)
        self.valor = valor

    def avaliar_condicao(self):
        return self.dispositivo.get_valor() != self.valor


class CondicaoPotenciometro(Condicao):
    __tablename__ = 'condicao_potenciometro'
    id_condicao = db.Column(db.Integer(), db.ForeignKey("condicao.id_condicao"), primary_key=True)
    valor_inicial = db.Column(db.Float)
    valor_final = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor_inicial, valor_final):
        if isinstance(valor_inicial, int) or isinstance(valor_inicial, str):
            valor_inicial = float(valor_inicial)
        if isinstance(valor_final, int) or isinstance(valor_final, str):
            valor_final = float(valor_final)
        if not isinstance(valor_inicial, float) or not isinstance(valor_final, float):
            raise TypeError("Valor não é um float")
        if not isinstance(potenciometro, Potenciometro):
            raise TypeError("Dispositivo passado não é um Potenciometro")
        Condicao.__init__(self, potenciometro)
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final

    def avaliar_condicao(self):
        return self.valor_inicial <= self.dispositivo.get_valor() and self.dispositivo.get_valor() >= self.valor_final


class CondicaoSensor(Condicao):
    __tablename__ = 'condicao_sensor'
    id_condicao = db.Column(db.Integer(), db.ForeignKey("condicao.id_condicao"), primary_key=True)
    valor_inicial = db.Column(db.Float)
    valor_final = db.Column(db.Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, sensor, valor_inicial, valor_final, regra_atuadora):
        if isinstance(valor_inicial, int):
            valor_inicial = float(valor_inicial)
        if isinstance(valor_final, int):
            valor_final = float(valor_final)
        if not isinstance(valor_inicial, float) or not isinstance(valor_final, float):
            raise TypeError("Valor não é um float")
        if not isinstance(sensor, Sensor):
            raise TypeError("Dispositivo passado não é um Sensor")
        if not isinstance(regra_atuadora, RegraPotenciometro) and not isinstance(regra_atuadora, RegraInterruptor):
            raise TypeError("Regra atuadora não é valida")
        Condicao.__init__(self, sensor)
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final

    def avaliar_condicao(self):
        return self.valor_inicial <= self.dispositivo.get_valor() and self.dispositivo.get_valor() >= self.valor_final


class CondicaoInterruptorCronometrada(CondicaoInterruptor):
    __tablename__ = 'condicao_interruptor_cronometrada'
    id_condicao = db.Column(db.Integer(), db.ForeignKey("condicao_interruptor.id_condicao"), primary_key=True)
    hora = db.Column(db.Integer)
    minuto = db.Column(db.Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor, hora, minuto):
        CondicaoInterruptor.__init__(self, interruptor, valor)
        self.hora = hora
        self.minuto = minuto

    def avaliar_regra(self):
        return self.hora == datetime.now().hour and self.minuto == datetime.now().minute and self.dispositivo.get_valor() != self.valor


class CondicaoPotenciometroCronometrada(CondicaoPotenciometro):
    __tablename__ = 'condicao_potenciometro_cronometrada'
    id_condicao = db.Column(db.Integer(), db.ForeignKey("condicao_potenciometro.id_condicao"), primary_key=True)
    hora = db.Column(db.Integer)
    minuto = db.Column(db.Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor_inicial, valor_final, hora, minuto):
        CondicaoPotenciometro.__init__(self, potenciometro, valor_inicial, valor_final)
        self.hora = hora
        self.minuto = minuto

    def avaliar_regra(self):
        return self.hora == datetime.now().hour and self.minuto == datetime.now().minute and self.dispositivo.get_valor() != self.valor


class CondicaoSensorCronometrada(CondicaoSensor):
    __tablename__ = 'condicao_sensor_cronometrada'
    id_condicao = db.Column(db.Integer(), db.ForeignKey("condicao_sensor.id_condicao"), primary_key=True)
    hora = db.Column(db.Integer)
    minuto = db.Column(db.Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, sensor, valor_inicial, valor_final, regra_atuadora, hora, minuto):
        CondicaoSensor.__init__(self, sensor, valor_inicial, valor_final, regra_atuadora)
        self.hora = hora
        self.minuto = minuto

    def avaliar_regra(self):
        return self.valor_inicial <= self.dispositivo.get_valor() and self.dispositivo.get_valor() >= self.valor_final and self.hora == datetime.now().hour and self.minuto == datetime.now().minute


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

    def executar_regra(self, regra):
        raise TypeError('abstract method cannot be called')

    def after_run(self):
        raise TypeError('abstract method cannot be called')


class MonitorManual(Monitor):
    __tablename__ = 'monitor_manual'
    id_monitor = db.Column(db.Integer(), db.ForeignKey("monitor.id_monitor"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome):
        Monitor.__init__(self, nome)

    def before_run(self):
        raise Exception('not implemented')

    def run(self):
        raise Exception('not implemented')

    def verificar_regras(self):
        raise Exception('not implemented')

    def executar_regra(self, regra):
        raise Exception('not implemented')

    def after_run(self):
        raise Exception('not implemented')


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
        db.session.commit()
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
        # self.dispositivo.valor = self.after_execute()
        self.dispositivo.valor = self.valor
        db.session.commit()

    def after_execute(self):
        request = RequestLeitura()
        request.before_execute(self.embarcado.ip, self.dispositivo.porta)
        return request.execute()
