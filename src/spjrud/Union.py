import Expr

class Union(Expr):
""" cette classe represente l'union de deux relations """

	def __init__(self, relation1, relation2):
		self.relation1=relation1
		self.relation2=relation2
		self.exp= "Union("+relation1.exp+","+relation2.exp")"
