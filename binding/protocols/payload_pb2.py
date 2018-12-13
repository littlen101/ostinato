# Author: Kyle Ruiz, kruiz2015@my.fit.edu
# Payload class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/payload_pb2.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_payload.html

class Payload:
	#DataPatternMode 
	e_dp_fixed_word = 0
	e_dp_inc_byte = 1
	e_dp_dec_byte = 2
	e_dp_random = 3
	
		
	def __init__(self, pattern_mode, pattern = 0):
		self.pattern_mode = pattern_mode
		self.pattern = int(pattern)
		return	
