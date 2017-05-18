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
