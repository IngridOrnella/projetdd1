import Expr

class Difference(Expr):
""" cette classe represente un attribut qui est representé par son nom """

	def __init__(self, relation1, relation2):
		self.relation1=relation1
		self.relation2=relation2
		self.exp= "Diff("+relation1.exp+","+relation2.exp")"
