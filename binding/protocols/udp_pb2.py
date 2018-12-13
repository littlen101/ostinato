# Author: Kyle Ruiz,
#kruiz2015@my.fit.edu
#udp_class

class Udp:
	def __init__ (self, is_override_src_port = False, is_override_dst_port = False, is_override_totlen = False, is_override_cksum = False, src_port = 49152, dst_port = 49153, totlen = 0, cksum = 0):
		self.is_override_src_port = bool(is_override_src_port)
		self.is_override_dst_port = bool(is_override_dst_port)
		self.is_override_totlen = bool(is_override_totlen)
		self.is_override_cksum = bool(is_override_ckscum)
		self.src_port = int(src_port)
		self.dst_port = int(dst_port)
		self.totlen = int(totlen)
		self.cksum = int(cksum)
		return