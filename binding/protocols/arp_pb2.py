# Author: Alex Winstead, awinstead2015@my.fit.edu
# Arp class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/arp.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_arp.html

class Arp:
    #constants
    #HwAddrMode
    kFixed = 0
    kIncrement = 1
    kDecrement = 2
    #ProtoAddrMode
    kFixedHost = 0
    kIncrementHost = 1
    kDecrementHost = 2
    kRandomHost = 3
    
    def __init__(self, hw_type = 1, proto_type = 2048, hw_addr_len = 6,
                 proto_addr_len = 4, op_code = 1, sender_hw_addr = 0,
                 sender_hw_addr_mode = kFixed, sender_hw_addr_count = 16,  
                 sender_proto_addr = 0, sender_proto_addr_mode = kFixedHost,
                 sender_proto_addr_count = 16, sender_proto_addr_mask = 4294967040,
                 target_hw_addr = 0, target_hw_addr_mode = kFixed, target_hw_addr_count = 16,
                 target_proto_addr = 0, target_proto_addr_mode = kFixedHost,
                 target_proto_addr_count = 16, target_proto_addr_mask = 4294967040):
        self.hw_type = int(hw_type)
        self.proto_type = int(proto_type)
        self.hw_addr_len = int(hw_addr_len)
        self.proto_addr_len = int(proto_addr_len)
        self.op_code = int(op_code)
        self.sender_hw_addr = int(sender_hw_addr)
        self.sender_hw_addr_mode = HwAddrMode(sender_hw_addr_mode)
        self.sender_hw_addr_count = int(sender_hw_addr_count)
        self.sender_proto_addr = int(sender_proto_addr)
        self.sender_proto_addr_mode = ProtoAddrMode(sender_proto_addr_mode)
        self.sender_proto_addr_count = int (sender_proto_addr_count)
        self.sender_proto_addr_mask = int (sender_proto_addr_mask)
        self.target_hw_addr = int (target_hw_addr)
        self.target_hw_addr_mode = HwAddrMode(target_hw_addr_mode)
        self.target_hw_addr_count = int(target_hw_addr_count)
        self.target_proto_addr = int(target_proto_addr)
        self.target_proto_addr_mode = ProtoAddrMode(target_proto_addr_mode)
        self.target_proto_addr_count = int(target_proto_addr_count)
        self.target_proto_addr_mask = int(target_proto_addr_mask)
        return
