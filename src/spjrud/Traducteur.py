from Compilateur import *
from Expr import * 
from Attribut import *
from Selection import *
from Constante import *
from Relation import *
from Egal import *
from Projection import *
from Jointure import *
from Rename import *
from Union import *
from Difference import *

 

class Traducteur():

	def traduction(self, spjrud):
		self.spjrud.verification()
		return spjrud
