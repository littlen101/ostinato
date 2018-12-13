# Author: Alex Winstead, awinstead2015@my.fit.edu
#icmp class
#corrisponding .proto file :
#https://github.com/littlen101/ostinato/blob/master/common/icmp.proto

#Corrisponding API guide:
#https://apiguide.ostinato.org/module_icmp.html

class Icmp:
    #Class Constants
    kIcmp4 = 4
    kIcmp6 = 6

    #Had to use type1 cause type is restricted pyhton name.
    def __init__(self, icmp_version = kIcmp4, is_override_checksum = False,
                 type1 = 8, code = 0, checksum = 0, identifier = 1234,
                 sequence = 0):
        self.icmp_version = Version(icmp_version)
        self.is_override_checksum = bool(is_override_checksum)
        self.type1 = int(type1)
        self.code = int(code)
        self.checksum = int(checksum)
        self.identifier = int(identifier)
        self.sequence = int(sequence)
