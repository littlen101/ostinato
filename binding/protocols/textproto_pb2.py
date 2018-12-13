# Author: Kyle Ruiz,
#kruiz2015@my.fit.edu
#Text_proto

class TextProtocol:
	#constants
	
	#End of Line
	kCr = 0
	kLf = 1
	kCrLf = 2
	#Text Encoding (UTF-8)
	kUtf8 = 0
	def __init__(self, port_num = 80, encoding = kUtf8, text = " ", eol = kLf):
		self.port_num = int(port_num)
		self.encoding = encoding
		self.text = text
		self.eol = eol
		return
		
