import sqlite3
import Traducteur

class Compilateur():
	"""cette classe permet de traduire les requetes spjrud en sql"""

	def selectionBd(self,bd):
		global database
		database = self.bd

	 def traduction(self):
	 	try:
	 		trad = Traducteur()
	 		print(trad.traduction(spjrud).string_req())
	 		return True
	 	except TypeError as err:
	 		print(err.args)
	 		return False


