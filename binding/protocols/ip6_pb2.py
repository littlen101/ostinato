#Author: Alex Winstead, awinstead2015@my.fit.edu
#ip6 class
#corrisponding .proto file :
#https://github.com/littlen101/ostinato/blob/master/common/ip6.proto

#Corrisponding API guide:
#https://apiguide.ostinato.org/module_ip6.html

class Ip6:
    #Class Constants
    kFixed = 0
    kIncHost = 1
    kDecHost = 2
    kRandomHost = 3

    def __init__(self, is_override_version = False, is_override_payload_length = False,
                 is_override_header = False, version = 6, traffic_class = 0,
                 flow_label = 0, payload_length = 0, next_header = 0, hop_limit = 127,
                 src_addr_hi = 127, src_addr_lo = 0, src_addr_mode = kFixed,
                 src_addr_count = 16, src_addr_prefix = 64,
                 dst_addr_hi = 0, dst_addr_lo = 0, dst_addr_mode = kFixed,
                 dst_addr_count = 16, dst_addr_prefix = 64):
        self.is_override_version = bool(is_override_version)
        self.is_override_payload_length = bool(override_payload_length)
        self.is_override_next_header = bool(is_override_header)
        self.version = int(version)
        self.traffic_class = int(traffic_class)
        self.flow_label = int(flow_label)
        self.payload_length = int(payload_length)
        self.next_header = int(next_header)
        self.hop_limit = int(hop_limit)
        self.src_addr_hi = int(src_addr_hi)
        self.src_addr_lo = int(src_addr_lo)
        self.src_addr_mode = AddrMode(src_addr_mode)
        self.src_addr_count = int(src_addr_count)
        self.dst_addr_hi = int(dst_addr_hi)
        self.dst_addr_lo = int(dst_addr_lo)
        self.dst_addr_mode = AddrMode(dst_addr_mode)
        self.dst_addr_count = int(dst_addr_count)
        self.dst_addr_prefix = int(dst_addr_prefix)
