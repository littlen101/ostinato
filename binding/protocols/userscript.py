# Author: Kyle Ruiz, kruiz2015@my.fit.edu
# UserScript class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/userscript_pb2.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_userscript.html

class UserScript:
	def __init__ (self, program = " "):
		self.program = str(program)
		return