import sqlite3
import Expr

class Projection(Expr):
	"""Cette classe represente la projection d'un attribut sur une relation"""
	def __init__(self, attribut, relation):
		self.attribut=attribut
		self.relation=relation
		self.exp= "Proj("+attribut.exp+","+relation.exp")"
		