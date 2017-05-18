class AbstractName(object):
	def __init__(self, nome=None):
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

class Propriedade(AbstractName):
	"""docstring for Propriedade"""
	def __init__(self, nome=None, components=[], usuarios=[]):
		super().__init__(nome)
		self.components = components
		self.usuarios = usuarios

	def add_usuario(self, usuario):
		if not(isinstance(usuario, Usuario)):
			raise TypeError('Precisa ser um objeto do tipo Usuario')
		self.usuarios.append(usuario)

	def add_component(self, component):
		if not(isinstance(component, Component)):
			raise TypeError('Precisa ser um objeto do tipo Component')
		self.components.append(component)
