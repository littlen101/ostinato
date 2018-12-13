# Author: Kyle Ruiz,
#kruiz2015@my.fit.edu
#snap class

class snap:
	def __init__ (self, is_override_oui = False, is_override_type = False, oui = 0, type = 0):
		self.is_override_oui = bool(is_override_oui)
		self.is_override_type = bool(is_override_type)
		self.oui = int(oui)
		self.type = int(type)
		return