import Expr
import Relation
import Constante
import Attribut

class Renommage(Expr):
	"""Cette classe represente le renommage d'un attribut"""


	def __init__(self,nom_depart, nom_final, relation):
		self.relation= relation
		self.nom_final= nom_final
		self.nom_depart=nom_depart
		self.col= relation.col
		self exp= "Rename("+self.nom_depart+","+self.nom_final+","+self.relation.exp+")"


	def __str__(self):
		return self.requete


	def rename(self):

	"""cette methode permet de renommer"""
		for i in self.col:
			if(i==self.nom_depart):
				self.col[i][0]= self.nom_final


	def verification(self):
		if (op.eq(self.relation,Expr)):
			self.relation.verification()
		if(op.eq(self.relation,Relation)):
			if(!self.relation.verifieRelation()):
				raise TypeError("cette table n'existe pas dans la base de données")
		self.verifie_type()
		self.requete="SELECT "+str(self.nom_depart)+" AS "+str(self.nom_final)+" FROM "+str(self.relation)
		self.rename()

	def verifie_type(self):
		if((!op.eq(self.relation,Relation) or !op.eq(self.relation,Expr))):
			raise TypeError("l'atribut doit etre une relation ou une expression")
		elif (!op.eq(self.nom_depart,Attribut)):
			raise TypeError("le nom de depart doit etre un attribut")
		elif(!op.eq(self.nom_final,Constante)):
			raise TypeError("le nom de renommage doit etre une constante")