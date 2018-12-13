# Author: Kyle Ruiz, kruiz2015@my.fit.edu
# Mac class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/mac.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_mac.html

class Mac:
	#MacAddrMode
	e_mm_fixed = 0
	e_mm_inc = 1
	e_mm_dec = 2
	e_mm_resolve = 3
	
	def __init__(self, dst_mac = 0, dst_mac_mode = e_mm_fixed, dst_mac_count = 16, dst_mac_step = 1, src_mac = 0, src_mac_mode = e_mm_fixed, src_mac_count = 16, src_mac_step = 1):
		self.dst_mac = int(dst_mac)
		self.dst_mac_mode = dst_mac_mode
		self.dst_mac_count = int(dst_mac_count)
		self.dst_mac_step = int(dst_mac_step)
		self.src_mac = int(src_mac)
		self.src_mac_mode = src_mac_mode
		self.src_mac_count = int(src_mac_count)
		self.src_mac_step = int(src_mac_step)
		return
