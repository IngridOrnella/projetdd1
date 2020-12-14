import sqlite3

class Relation(object):
	"""Constructeur de Relation"""
	def __init__(self,nom):
		self.nom = nom



	def getRelationType(self, nom):
		""" Cette methode permet d'avoir les informations sur les types des colonnes dans une table"""
		try:
			con = sqlite3.connect(database)
			cur = con.cursor()
			requete = "PRAGMA table_info("+str(nom)+");" #permet d'avoirles informations sur la table
			cur.execute(requete)
			col =[]
			info =cur.fetchall()
			for i in info:
				nom_type = [i[1], i[2]]
				col.append(nom_type)

			cur.close()
		except sqlite3.Error as err:
			print("erreur de lecture des donnees dans la table", err)

		finally:
			if(con):
				con.close()
				print("connection fermée")

		
