import Expr

class Jointure(Expr):
""" cette classe represente une jointure entre deux relations"""

	def __init__(self, relation1, relation2):
		self.relation1=relation1
		self.relation2=relation2
		self.exp= "Join("+relation1.exp+","+relation2.exp")"
