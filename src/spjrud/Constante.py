import Expr


class Constante(Expr):
	"""Cette classe represente une constante dans SPJRUD"""


	def __init__(self,nom):
		self.nom= nom
		self.exp= "Cst("+str(nom)+")" 


	def __str__(self):
		return "'"+self.nom+"'"
		

