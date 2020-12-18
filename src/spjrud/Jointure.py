import Expr

class Jointure(Expr):
""" cette classe represente une jointure entre deux relations"""

	def __init__(self, relation1, relation2):
		self.relation1=relation1
		self.relation2=relation2
		self.exp= "Join("+relation1.exp+","+relation2.exp")"



	def verification(self):
		if (op.eq(self.relation1,Expr)):
			self.relation1.verification()
		if (op.eq(self.relation2,Expr)):
			self.relation2.verification()
		if(op.eq(self.relation1,Relation)):
			if(!self.relation1.verifieRelation()):
				raise TypeError("cette table n'existe pas dans la base de données")
		if(op.eq(self.relation2,Relation)):
			if(!self.relation2.verifieRelation()):
				raise TypeError("cette table n'existe pas dans la base de données")
		self.verifieTypes(self.relation1,self.relation2)
		self.requete ="SELECT * FROM "+str(self.relation1)+" JOIN SELECT * FROM "+str(self.relation2)

	def __str__(self):
		return self.requete



	def verifie_type(self):
		if((!op.eq(self.relation1,Relation) or !op.eq(self.relation1,Expr))):
			raise TypeError("l'atribut doit etre une relation ou une expression")
		elif((!op.eq(self.relation2,Relation) or !op.eq(self.relation2,Expr))):
			raise TypeError("l'atribut doit etre une relation ou une expression")


