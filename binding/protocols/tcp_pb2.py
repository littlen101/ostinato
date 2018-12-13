# Author: Kyle Ruiz, kruiz2015@my.fit.edu
# Tcp class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/tcp_pb2.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_tcp.html

class Tcp:
	def __init__ (self, is_override_src_port = False, is_override_dst_port = False, is_override_hdrlen = False, is_override_cksum = False, src_port = 49152, dst_port = 49153, seq_num = 129018, ack_num = 0, hdrlen_rsvd = 80, flags = 0, window = 1024, cksum = 0, urg_ptr = 0):
		self.is_override_src_port = bool(is_override_src_port)
		self.is_override_dst_port = bool (is_override_dst_port)
		self.is_override_hdrlen = bool (is_override_src_port )
		self.is_override_cksum = is_override_cksum
		self.src_port = int(src_port)
		self.dst_port = int(dst_port)
		self.seq_num = int(seq_num)
		self.ack_num = int(ack_num)
		self.hdrlen_rsvd = int(hdrlen_rsvd)
		self.flags = int(flags)
		self.window = int(window)
		self.cksum = int(cksum)
		self.urg_ptr = urg_ptr
		return
