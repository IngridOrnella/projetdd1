import sqlite3
import Relation

class Expr(SPRJUD):
	"""Cette classe represente une expression ecrite en spjrud. elle est la classe mere de notre AST"""


	def __init__(self,relation):
		self.relation = relation
		self.col= relation.col 


	def __str__(self):
		return

	def print_req(self):
		print(self.requete)

	def string_req(self):
		return self.requete
		


