# Author: Kyle Ruiz,
#kruiz2015@my.fit.edu
#Vlan_class
class Vlan:
	def __init__(self, is_override_tpid = False, tpid = 1, vlan_tag = 0):
		self.is_override_tpid = bool(is_override_tpid)
		self.tpid = int(tpid)
		self.vlan_tag = int(vlan_tag)	
		return
