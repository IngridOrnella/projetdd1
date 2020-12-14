
class Attribut(nom):
""" cette classe represente un attribut qui est representé par son nom """

	def __init__(self,nom):
		self.nom= nom
		self.exp = "("+nom+")"


	def __str__(self):
		return self.nom