#Author: Alex Winstead, awinstead2015@my.fit.edu
#Eth2 class
#corrisponding .proto file :
#https://github.com/littlen101/ostinato/blob/master/common/eth2.proto

#Corrisponding API guide:
#https://apiguide.ostinato.org/module_eth2.html


class Eth2:
    def __init__(self, is_override_type = False, type = 0):
        self.is_override_type = bool(is_override_type)
        self.type = int(type)
        return
