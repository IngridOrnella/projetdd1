import Expr
import Relation

class Renommage(Expr):
	"""Cette classe represente le renommage d'un attribut"""


	def __init__(self,nom_depart, nom_final, relation):
		self.relation= relation
		self.col= relation.col 


	def __str__(self):
		return self.nom
		

