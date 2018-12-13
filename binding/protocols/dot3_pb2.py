# Author: Alex Winstead, awinstead2015@my.fit.edu
# Dot3 class
# corrisponding .proto file :
# https://github.com/littlen101/ostinato/blob/master/common/dot3.proto

# Corrisponding API guide:
# https://apiguide.ostinato.org/module_dot3.html


class Dot3:
    def __init__(self, is_override_length = False, length = 0):
        self.is_override_length = bool(is_override_length)
        self.length = int(length)
        return
