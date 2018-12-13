# Author: Kyle Ruiz, kruiz2015@my.fit.edu
# Snap class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/snap_pb2.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_snap.html

class Snap:
	def __init__ (self, is_override_oui = False, is_override_type = False, oui = 0, type = 0):
		self.is_override_oui = bool(is_override_oui)
		self.is_override_type = bool(is_override_type)
		self.oui = int(oui)
		self.type = int(type)
		return
