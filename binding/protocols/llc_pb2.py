# Author: Kyle Ruiz,
#kruiz2015@my.fit.edu
#llc_pb2

class Llc:
	def __init__(is_override_dsap = False, is_override_ssap = False, is_override_ctl = False, dsap = 0, ssap = 0, ctl = 0):
		self.is_override_dsap = bool(is_override_dsap)
		self.is_override_ssap = bool(is_override_ssap)
		self.is_override_ctl = bool(is_override_ctl)
		self.dsap = int(dsap)
		self.ssap = int(ssap)
		self.ctl = int(ctl)
		return