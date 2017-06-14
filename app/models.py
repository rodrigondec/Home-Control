# from app import db
from threading import Thread
import time
from time import sleep
from datetime import datetime
from database import Base
# from app import Session
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Float, Boolean, DateTime, func
from sqlalchemy.orm import relationship, backref
from database import Session

db_session = Session()

# Many-to-many helper tables (for public access, use Bases only) -----------

modulo_usuario = Table(
    'modulo_usuario',
    Base.metadata,
    Column(
        'id_component',
        Integer,
        ForeignKey('modulo_privado.id_component')
    ),
    Column(
        'id_usuario',
        Integer,
        ForeignKey('usuario.id_usuario')
    )
)

modulo_component = Table(
    'modulo_component',
    Base.metadata,
    Column(
        'id_component_pai',
        Integer,
        ForeignKey('modulo.id_component')
    ),
    Column(
        'id_component_filho',
        Integer,
        ForeignKey('component.id_component'),
        unique=True
    )
)


# Bases and their simple relantionships -------------------------------------


class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String(80))
    email = Column(String(50), unique=True)
    senha = Column(String(64))

    tipo = Column(String(30))
    __mapper_args__ = {'polymorphic_identity': __tablename__,
                       'polymorphic_on': tipo}

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Administrador(Usuario):
    __tablename__ = 'administrador'
    id_usuario = Column(Integer(), ForeignKey("usuario.id_usuario", ondelete="CASCADE"), primary_key=True)

    client_id = Column(Integer, ForeignKey('client.id_client'))
    client = relationship("Client", uselist=False, back_populates='administrador')

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, email, senha):
        Usuario.__init__(self, nome, email, senha)


class Client(Base):
    __tablename__ = 'client'
    id_client = Column(Integer, primary_key=True)

    administrador = relationship("Administrador", uselist=False, back_populates="client")

    component_id = Column(Integer, ForeignKey('component.id_component'))
    component = relationship("Component", uselist=False)


class Component(Base):
    __tablename__ = 'component'
    id_component = Column(Integer, primary_key=True)
    nome = Column(String(80))

    tipo = Column(String(30))
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
    id_component = Column(Integer(),
                             ForeignKey("component.id_component", ondelete="CASCADE"), primary_key=True)

    embarcado = relationship("Embarcado", uselist=False, back_populates="leaf")

    dispositivos = relationship("Dispositivo", back_populates="leaf")

    monitor = relationship("Monitor", uselist=False, back_populates="leaf")

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
    id_component = Column(Integer(), ForeignKey("component.id_component"), primary_key=True)

    components = relationship(
        'Component',
        secondary=modulo_component,
        backref=backref('component_modulo', lazy='dynamic')
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
    id_component = Column(Integer(), ForeignKey("modulo.id_component"), primary_key=True)

    usuarios = relationship(
        'Usuario',
        secondary=modulo_usuario,
        backref=backref('modulos', lazy='dynamic')
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


class Embarcado(Base):
    __tablename__ = 'embarcado'
    id_embarcado = Column(Integer, primary_key=True)
    ip = Column(String(15))
    mac = Column(String(20))

    leaf_id = Column(Integer, ForeignKey('leaf.id_component'))
    leaf = relationship("Leaf", back_populates="embarcado")

    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac


class Dispositivo(Base):
    __tablename__ = 'dispositivo'
    id_dispositivo = Column(Integer, primary_key=True)
    nome = Column(String(80))
    porta = Column(Integer)

    leaf_id = Column(Integer, ForeignKey('leaf.id_component'))
    leaf = relationship("Leaf", back_populates="dispositivos")

    usos = relationship("Uso", back_populates="dispositivo")

    atuadores = relationship("Atuador", back_populates="dispositivo")

    condicoes = relationship("Condicao", back_populates="dispositivo")

    tipo = Column(String(30))
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
    id_dispositivo = Column(Integer(), ForeignKey("dispositivo.id_dispositivo"), primary_key=True)
    valor = Column(Float())

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, porta):
        Dispositivo.__init__(self, nome, porta)

    def get_valor(self):
        return self.valor


class Interruptor(Dispositivo):
    __tablename__ = 'interruptor'
    id_dispositivo = Column(Integer(), ForeignKey("dispositivo.id_dispositivo"), primary_key=True)
    valor = Column(Boolean())

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, porta):
        Dispositivo.__init__(self, nome, porta)

    def get_valor(self):
        return self.valor


class Potenciometro(Dispositivo):
    __tablename__ = 'potenciometro'
    id_dispositivo = Column(Integer(), ForeignKey("dispositivo.id_dispositivo"), primary_key=True)
    valor = Column(Float())

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, nome, porta):
        Dispositivo.__init__(self, nome, porta)

    def get_valor(self):
        return self.valor


class Uso(Base):
    __tablename__ = 'uso'
    id_uso = Column(Integer, primary_key=True)
    hora = Column(DateTime, default=func.now())
    usuario_id = Column(Integer)

    dispositivo_id = Column(Integer, ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = relationship("Dispositivo", back_populates="usos")

    tipo = Column(String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, dispositivo, usuario_id):
        if self.__class__ is Regra:
            raise TypeError('abstract class cannot be instantiated')
        self.dispositivo = dispositivo
        self.usuario_id = usuario_id


class UsoInterruptor(Uso):
    __tablename__ = 'uso_interruptor'
    id_uso = Column(Integer(), ForeignKey("uso.id_uso"), primary_key=True)
    valor = Column(Boolean)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor, usuario_id):
        if not isinstance(valor, bool):
            raise TypeError("Valor não é um boolean")
        Uso.__init__(self, interruptor, usuario_id)
        self.valor = valor


class UsoPotenciometro(Uso):
    __tablename__ = 'uso_potenciometro'
    id_uso = Column(Integer(), ForeignKey("uso.id_uso"), primary_key=True)
    valor = Column(Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor, usuario_id):
        if not isinstance(valor, float):
            raise TypeError("Valor não é um boolean")
        Uso.__init__(self, potenciometro, usuario_id)
        self.valor = valor


class Regra(Base):
    __tablename__ = 'regra'
    id_regra = Column(Integer, primary_key=True)

    monitor_id = Column(Integer, ForeignKey('monitor.id_monitor'))
    monitor = relationship("Monitor", back_populates="regras")

    condicao = relationship("Condicao", uselist=False, back_populates="regra")

    atuador = relationship("Atuador", uselist=False, back_populates="regra")

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
        valor1 = self.condicao.avaliar_condicao()
        valor2 = self.atuador.dispositivo.valor != self.atuador.valor
        return valor1 and valor2

    def execute(self):
        self.atuador.execute()


class Atuador(Base):
    __tablename__ = 'atuador'
    id_atuador = Column(Integer, primary_key=True)

    regra_id = Column(Integer, ForeignKey('regra.id_regra'))
    regra = relationship("Regra", back_populates="atuador")

    dispositivo_id = Column(Integer, ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = relationship("Dispositivo", back_populates="atuadores")

    tipo = Column(String(30))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, dispositivo):
        if self.__class__ is Atuador:
            raise TypeError('abstract class cannot be instantiated')
        self.dispositivo = dispositivo

    def execute(self):
        raise TypeError('abstract method cannot be called')


class AtuadorInterruptor(Atuador):
    __tablename__ = 'atuador_interruptor'
    id_atuador = Column(Integer(), ForeignKey("atuador.id_atuador"), primary_key=True)
    valor = Column(Boolean)

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
        command = Command.query.filter_by(tipo='alterar_dispositivo').first()
        command.before_execute(self.dispositivo.leaf.embarcado, self.dispositivo, self.valor)
        command.execute()


class AtuadorPotenciometro(Atuador):
    __tablename__ = 'atuador_potenciometro'
    id_atuador = Column(Integer(), ForeignKey("atuador.id_atuador"), primary_key=True)
    valor = Column(Float)

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
        command = Command.query.filter_by(tipo='alterar_dispositivo').first()
        command.before_execute(self.dispositivo.leaf.embarcado, self.dispositivo, self.valor)
        command.execute()


class Condicao(Base):
    __tablename__ = 'condicao'
    id_condicao = Column(Integer, primary_key=True)

    regra_id = Column(Integer, ForeignKey('regra.id_regra'))
    regra = relationship("Regra", back_populates="condicao")

    dispositivo_id = Column(Integer, ForeignKey('dispositivo.id_dispositivo'))
    dispositivo = relationship("Dispositivo", back_populates="condicoes")

    tipo = Column(String(40))
    __mapper_args__ = {'polymorphic_on': tipo}

    def __init__(self, dispositivo):
        if self.__class__ is Condicao:
            raise TypeError('abstract class cannot be instantiated')
        self.dispositivo = dispositivo

    def avaliar_condicao(self):
        raise TypeError('abstract method cannot be called')


class CondicaoInterruptor(Condicao):
    __tablename__ = 'condicao_interruptor'
    id_condicao = Column(Integer(), ForeignKey("condicao.id_condicao"), primary_key=True)
    valor = Column(Boolean)

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

    def __str__(self):
        return 'valor == '+str(self.valor)

    def avaliar_condicao(self):
        valor = self.dispositivo.get_valor() == self.valor
        return valor


class CondicaoPotenciometro(Condicao):
    __tablename__ = 'condicao_potenciometro'
    id_condicao = Column(Integer(), ForeignKey("condicao.id_condicao"), primary_key=True)
    valor_inicial = Column(Float)
    valor_final = Column(Float)

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

    def __str__(self):
        return str(self.valor_inicial)+' <= valor >= '+str(self.valor_final)

    def avaliar_condicao(self):
        return self.valor_inicial <= self.dispositivo.get_valor() and self.dispositivo.get_valor() >= self.valor_final


class CondicaoSensor(Condicao):
    __tablename__ = 'condicao_sensor'
    id_condicao = Column(Integer(), ForeignKey("condicao.id_condicao"), primary_key=True)
    valor_inicial = Column(Float)
    valor_final = Column(Float)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, sensor, valor_inicial, valor_final):
        if isinstance(valor_inicial, int):
            valor_inicial = float(valor_inicial)
        if isinstance(valor_final, int):
            valor_final = float(valor_final)
        if not isinstance(valor_inicial, float) or not isinstance(valor_final, float):
            raise TypeError("Valor não é um float")
        if not isinstance(sensor, Sensor):
            raise TypeError("Dispositivo passado não é um Sensor")
        Condicao.__init__(self, sensor)
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final

    def __str__(self):
        return str(self.valor_inicial)+' <= valor >= '+str(self.valor_final)

    def avaliar_condicao(self):
        return self.valor_inicial <= self.dispositivo.get_valor() and self.dispositivo.get_valor() >= self.valor_final


class CondicaoInterruptorCronometrada(CondicaoInterruptor):
    __tablename__ = 'condicao_interruptor_cronometrada'
    id_condicao = Column(Integer(), ForeignKey("condicao_interruptor.id_condicao"), primary_key=True)
    hora = Column(Integer)
    minuto = Column(Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, interruptor, valor, hora, minuto):
        CondicaoInterruptor.__init__(self, interruptor, valor)
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return 'valor == '+str(self.valor)+' and hora == '+str(self.hora)+':'+str(self.minuto)

    def avaliar_regra(self):
        return self.hora == datetime.now().hour and self.minuto == datetime.now().minute and self.dispositivo.get_valor() != self.valor


class CondicaoPotenciometroCronometrada(CondicaoPotenciometro):
    __tablename__ = 'condicao_potenciometro_cronometrada'
    id_condicao = Column(Integer(), ForeignKey("condicao_potenciometro.id_condicao"), primary_key=True)
    hora = Column(Integer)
    minuto = Column(Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, potenciometro, valor_inicial, valor_final, hora, minuto):
        CondicaoPotenciometro.__init__(self, potenciometro, valor_inicial, valor_final)
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return str(self.valor_inicial)+' <= valor >= '+str(self.valor_final)+' and hora == '+str(self.hora)+':'+str(self.minuto)

    def avaliar_regra(self):
        return self.hora == datetime.now().hour and self.minuto == datetime.now().minute and self.dispositivo.get_valor() != self.valor


class CondicaoSensorCronometrada(CondicaoSensor):
    __tablename__ = 'condicao_sensor_cronometrada'
    id_condicao = Column(Integer(), ForeignKey("condicao_sensor.id_condicao"), primary_key=True)
    hora = Column(Integer)
    minuto = Column(Integer)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self, sensor, valor_inicial, valor_final, hora, minuto):
        CondicaoSensor.__init__(self, sensor, valor_inicial, valor_final)
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return str(self.valor_inicial) + ' <= valor >= ' + str(self.valor_final) + ' and hora == ' + str(
            self.hora) + ':' + str(self.minuto)

    def avaliar_regra(self):
        return self.valor_inicial <= self.dispositivo.get_valor() and self.dispositivo.get_valor() >= self.valor_final and self.hora == datetime.now().hour and self.minuto == datetime.now().minute


class Monitor(Base):
    __tablename__ = 'monitor'
    id_monitor = Column(Integer, primary_key=True)
    nome = Column(String(80))

    leaf_id = Column(Integer, ForeignKey('leaf.id_component'))
    leaf = relationship("Leaf", back_populates="monitor")

    regras = relationship("Regra", back_populates="monitor")

    def __init__(self, nome):
        self.nome = nome

    def add_regra(self, regra):
        if regra in self.regras:
            raise Exception("Regra duplicada")
        self.regras.append(regra)

    def remove_regra(self, regra):
        self.regras.remove(regra)

    def start(self):
        self.running = True
        self.thread = Thread(target=self.run)
        self.thread.start()

    def before_run(self):
        pass

    def run(self):
        self.before_run()
        while self.running:
            # db_session.expire_all()
            print('Monitor '+str(self.id_monitor)+' vai verificar regras!')
            self.verificar_regras()
            print('Monitor ' + str(self.id_monitor) + ' vai dormir por 5 segundos!')
            sleep(5)
        self.after_run()

    def verificar_regras(self):
        for regra in self.regras:
            db_session = Session()
            regra = db_session.query(Regra).filter_by(id_regra=regra.id_regra).first()
            if regra.avaliar_regra():
                print('Regra '+str(regra.id_regra)+' foi ativada!')
                self.executar_regra(regra)
            db_session.close()
            Session.remove()

    def executar_regra(self, regra):
        print('Monitor '+str(self.id_monitor)+' executando regra '+str(regra.id_regra)+'!')
        regra.execute()

    def after_run(self):
        pass


class Command(Base):
    __tablename__ = 'command'
    id_command = Column(Integer, primary_key=True)

    tipo = Column(String(30))
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
    id_command = Column(Integer(), ForeignKey("command.id_command"), primary_key=True)

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
    id_command = Column(Integer(), ForeignKey("command.id_command"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self):
        Command.__init__(self)

    def before_execute(self, ip, porta, valor):
        self.ip = ip
        self.porta = porta
        self.valor = valor

    def execute(self):
        # MOCK DE UM REQUEST HTTP para o servidor http://self.ip/self.porta/valor
        self.after_execute()

    def after_execute(self):
        pass


class AtualizarDispositivo(Command):
    __tablename__ = 'atualizar_dispositivo'
    id_command = Column(Integer(), ForeignKey("command.id_command"), primary_key=True)

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
        db_session.commit()
        db_session.flush()
        db_session.expire_all()
        self.after_execute()

    def after_execute(self):
        pass


class AlterarDispositivo(Command):
    __tablename__ = 'alterar_dispositivo'
    id_command = Column(Integer(), ForeignKey("command.id_command"), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': __tablename__}

    def __init__(self):
        Command.__init__(self)

    def before_execute(self, embarcado, dispositivo, valor, usuario_id=None):
        if not isinstance(embarcado, Embarcado):
            raise TypeError("parâmetro 1 precisa ser do tipo Embarcado")
        if not isinstance(dispositivo, Potenciometro) and not isinstance(dispositivo, Interruptor):
            raise TypeError("parâmetro 2 precisa ser do tipo Potenciometro ou Interruptor")
        self.embarcado = embarcado
        self.dispositivo = dispositivo
        self.valor = valor
        self.usuario_id = usuario_id

    def execute(self):
        request = RequestEscrita()
        request.before_execute(self.embarcado.ip, self.dispositivo.porta, self.valor)
        request.execute()
        # self.dispositivo.valor = self.after_execute()
        self.dispositivo = db_session.merge(self.dispositivo)
        self.dispositivo.valor = self.valor
        if self.usuario_id is not None:
            if self.dispositivo.tipo == 'interruptor':
                uso = UsoInterruptor(self.dispositivo, self.valor, self.usuario_id)
            else:
                uso = UsoPotenciometro(self.dispositivo, self.valor, self.usuario_id)
            db_session.add(uso)
        db_session.commit()
        db_session.flush()
        db_session.expire_all()

    def after_execute(self):
        request = RequestLeitura()
        request.before_execute(self.embarcado.ip, self.dispositivo.porta)
        return request.execute()
