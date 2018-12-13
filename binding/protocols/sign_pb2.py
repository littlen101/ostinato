# Author: Kyle Ruiz, kruiz2015@my.fit.edu
# Sign class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/sign_pb2.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_sign.html

class Sign:
	def __init__(self, stream_guid = 0):
		self.stream_guid = int(stream_guid)
		return