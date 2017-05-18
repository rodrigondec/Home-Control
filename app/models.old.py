class AbstractName(object):
	def __init__(self, nome):
		if self.__class__ is AbstractName:
			raise TypeError('abstract class cannot be instantiated')
		self.nome = nome

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, nome):
		self.__nome = nome

	def __str__(self):
		return self.nome

class Client(object):
	"""docstring for Client"""
	def __init__(self, root):
		if not(isinstance(root, Component)):
			raise TypeError('Precisa ser um objeto do tipo Component')
		self.root = root

	def add_component(self, component):
		self.root.add_component(component)

	def __str__(self):
		return self.root.nome

class Usuario(AbstractName):
	"""docstring for Usuario"""
	def __init__(self, nome, email, senha):
		super().__init__(nome)
		self.email = email
		self.senha = senha
	
	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, email):
		self.__email = email

	@property
	def senha(self):
		return self.__senha

	@senha.setter
	def senha(self, senha):
		self.__senha = senha

class Embarcado(object):
	"""docstring for Embarcado"""
	def __init__(self, ip):
		self.ip = ip
		
class Dispositivo(object):
	"""docstring for Dispositivo"""
	identificador=1
	def __init__(self):
		if self.__class__ is Dispositivo:
			raise TypeError('abstract class cannot be instantiated')
		self.identificador=Dispositivo.identificador
		Dispositivo.identificador += 1

class Sensor(Dispositivo):
	"""docstring for Sensor"""
	def __init__(self):
		super().__init__()
		self.arg = arg

class Interruptor(Dispositivo):
	"""docstring for Interruptor"""
	def __init__(self, arg):
		super().__init__()
		self.arg = arg

class Potenciometro(Dispositivo):
	"""docstring for Potenciometro"""
	def __init__(self, arg):
		self.arg = arg

class Uso(object):
	"""docstring for Uso"""
	def __init__(self, dispositivo=None, comando=None):
		super(Uso, self).__init__()
		self.dispositivo = dispositivo
		self.comando = comando
		
class Monitor(AbstractName):
	"""docstring for Monitor"""
	def __init__(self, nome):
		if self.__class__ is Monitor:
			raise TypeError('abstract class cannot be instantiated')
		super().__init__(nome)

class Component(AbstractName):
	"""docstring for Component"""
	def __init__(self, nome):
		super().__init__(nome)
		if self.__class__ is Component:
			raise TypeError('abstract class cannot be instantiated')

class Leaf(Component):
	"""docstring for Propriedade"""
	def __init__(self, nome, embarcado=None, dispositivos=[], monitor=None):
		super().__init__(nome)
		self.embarcado = embarcado
		self.dispositivos = dispositivos
		self.monitor = monitor

class Modulo(Component):
	"""docstring for Modulo"""
	def __init__(self, nome, components=[]):
		if self.__class__ is Modulo:
			raise TypeError('abstract class cannot be instantiated')
		super().__init__(nome)
		self.components = []

	def add_component(self, component):
		if not(isinstance(component, Component)):
			raise TypeError('Precisa ser um objeto do tipo Component')
		self.components.append(component)

class ModuloPublico(Modulo):
	"""docstring for ModuloPublico"""
	def __init__(self, nome, components=[]):
		super().__init__(nome, components)

class ModuloPrivado(Modulo):
	"""docstring for ModuloPublico"""
	def __init__(self, nome, components=[], usuarios=[]):
		super().__init__(nome, components)
		self.usuarios = usuarios

propriedade = Client(ModuloPrivado("Casa de rods"))
propriedade.add_component(Leaf("Jardim"))
print(propriedade)