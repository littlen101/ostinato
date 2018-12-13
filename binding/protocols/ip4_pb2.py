#Author: Alex Winstead, awinstead2015@my.fit.edu
#ip4 class
#corrisponding .proto file :
#https://github.com/littlen101/ostinato/blob/master/common/ip4.proto

#Corrisponding API guide:
#https://apiguide.ostinato.org/module_ip4.html

class Ip4:
    #Class Constants
    e_im_fixed = 0
    e_im_inc_host = 1
    e_im_dec_host = 2
    e_im_random_host = 3

    #should id be swithced?
    def __init__(self, is_override_ver = False, is_override_hdrlen = False,
                 is_override_totlen = False, is_override_proto = False,
                 is_override_cksum = False, ver_hdrlen = 69, tos = 0,
                 totlen = 0, id = 1234, flags = 0, frag_ofs = 0,
                 ttl = 127, proto = 0, cksum = 0, src_ip = 0, src_ip_mode = e_im_fixed,
                 src_ip_count = 16, src_ip_mask = 4294967040, dst_ip = 0,
                 dst_ip_mode = e_im_fixed, dst_ip_mask = 4294967040, options = ""):
        self.is_override_ver = bool(is_override_ver)
        self.is_override_hdrlen = bool(is_override_hdrlen)
        self.is_override_totlen = bool(is_override_totlen)
        self.is_override_proto = bool(is_override_proto)
        self.is_override_cksum = bool(is_override_cksum)
        self.ver_hdrlen = int(ver_hdrlen)
        self.tos = int(tos)
        self.totlen = int(totlen)
        self.id = int(id)
        self.flags = int(flags)
        self.frag_ofs = int(frag_ofs)
        self.ttl = int(ttl)
        self.proto = int(proto)
        self.cksum = int(cksum)
        self.src_ip = int(src_ip)
        self.src_ip_mode = IpAddrMode(src_ip_mode)
        self.src_ip_count = int(src_ip_count)
        self.src_ip_mask = int(src_ip_mask)
        self.dst_ip = int(dst_ip)
        self.dst_ip_mode = IpAddrMode(dst_ip_mode)
        self.dst_ip_count = int(dst_ip_count)
        self.options = str(options)
