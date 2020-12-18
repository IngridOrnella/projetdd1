import Expr
import operator as op
import Relation

class Difference(Expr):
""" cette classe represente un attribut qui est representé par son nom """

	def __init__(self, relation1, relation2):
		self.relation1=relation1
		self.relation2=relation2
		self.exp= "Diff("+relation1.exp+","+relation2.exp")"


	def arite_type(self, relation1,relation2):
		#methode qui permet de verifier l'arite des relations et leur types
		if (len(self.relation1.col) != len(self.relation2.col) ):
			raise TypeError("les deux relations n'ont pas la meme arité ou nombre de colonnes.")
		if((!op.eq(self.relation1,Relation) or !op.eq(self.relation1,Expr))):
			raise TypeError("l'atribut doit etre une relation ou une expression")
		if((!op.eq(self.relation2,Relation) or !op.eq(self.relation2,Expr))):
			raise TypeError("l'atribut doit etre une relation ou une expression")
			


	def verifieTypes(self, relation1,relation2):
		if (arite_type(self,relation1,relation2)):
			for i in range (len(self.relation1.col)):
				if (self.relation1.col[i][1] != self.relation2.col[i][1]):
					b =False
					raise TypeError("les deux relations n'ont pas le meme type")
					
	


	def verification(self):
		"""cette methode permet de verifier et traduire la requete"""
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
		self.arite_type(self.relation1,self.relation2)
		self.verifieTypes(self.relation1,self.relation2)
		self.requete = "SELECT * FROM "+str(self.relation1)+" MINUS SELECT * FROM "+str(self.relation2)


	def __str__(self):
		return self.requete
