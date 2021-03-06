# Author: Kyle Ruiz, kruiz2015@my.fit.edu
# Vlan class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/vlan_pb2.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_vlan.html

class Vlan:
	def __init__(self, is_override_tpid = False, tpid = 0, vlan_tag = 0):
		self.is_override_tpid = bool(is_override_tpid)
		self.tpid = int(tpid)
		self.vlan_tag = int(vlan_tag)	
		return
