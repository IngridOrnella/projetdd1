
import Expr

class Selection(Exp):
	"""Cette classe permet de traduiree la selection en algebre relationnel en sql"""

	def __init__(self,attribut,relation):
		#constructeur de l'operation de selection
		self.attribut=attribut
		self.relation=relation
		self.exp= "Select("+attribut.exp+","+relation.exp")" 