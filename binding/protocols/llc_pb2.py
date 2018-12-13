# Author: Alex Winstead, awinstead2015@my.fit.edu
# Llc class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/llc.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_llc.html

class Llc:
    #Had to use type1 cause type is restricted pyhton name.
    def __init__(self, is_override_dsap = False, is_override_ssap = False,
                 is_override_ctl = False, dsap = 0, ssap = 0, ctl = 0):
        self.is_override_dsap = bool(is_override_dsp)
        self.is_override_ssap = bool(is_override_ssap)
        self.is_override_ctl = bool(is_override_ctl)
        self.dsap = int(dsap)
        self.ssap = int(ssap)
        self.ctl = int(ctl)
