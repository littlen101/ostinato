# Author: Kyle Ruiz, kruiz2015@my.fit.edu
# Stp class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/stp_pb2.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_stp.html

class Stp:
	def __int__(self, protocol_id = 0, protocol_version_id = 0, bpdu_type = 0, flags = 0, root_id = 0, root_path_cost = 0, bridge_id = 0, port_id = 0, message_age = 0, max_age = 0, hello_time = 0, forward_delay = 0):
		self.protocol_id = int(protocol_id)
		self.protocol_version_id = int(protocol_version_id)
		self.bpdu_type = int(bpdu_type)
		self.flags = int(flags)
		self.root_id = int(root_id)
		self.root_path_cost = int(root_path_cost)
		self.bridge_id = int(bridge_id)
		self.port_id = int(port_id)
		self.message_age = int(message_age)
		self.max_age = int(max_age)
		self.hello_time = int(hello_time)
		self.forward_delay = int(forward_delay)
		return
