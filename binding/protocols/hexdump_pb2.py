#Author: Alex Winstead, awinstead2015@my.fit.edu
#Hexdump class
#corrisponding .proto file :
#https://github.com/littlen101/ostinato/blob/master/common/hexdump.proto

#Corrisponding API guide:
#https://apiguide.ostinato.org/module_hexdump.html

class HexDump:
    def __init__(self, content = "", pad_until_end = True):
        self.content = bool(content)
        self.pad_until_end = bool(pad_until_end)
        return
