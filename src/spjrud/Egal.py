import Attribut

class Egal(Expr):
""" cette classe represente l'operateur d'egalité"""

	def __init__(self, attr1, attr2):
		self.nom= nom
		self.exp= "("+attr1.exp+ "=" +attr2.exp+")"
	

	def __str__(self):
		return str(self.attr1)+" = "+str(self.attr2)
		
