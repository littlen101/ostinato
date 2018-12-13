# Author: Xuchao Jiang, xjiang2017@my.fit.edu
# ArpEntry, Device, DeviceNeighborList, Ip4Emulation, Ip6Address, Ip6Emulation, NdpEntry, MacEmulation, Vlan, VlanEmulation class
# emulproto_pb2.py
# Shortened as 'emul'
# API guide: https://apiguide.ostinato.org/module_emul.html
# Follows document guide instead of C++ files

class ArpEntry:
    def __init__(self, ip4=0, mac=0):
        self.ip4 = int(ip4)
        self.mac = int(mac)
        return

class Ip6Address:
    def __init__(self, hi=0, lo=0):
        self.hi = int(hi)
        self.lo = int(lo)
        return
    def __add__(self, other):
        sumLo = self.lo + other.lo
        sumHi = self.hi + other.hi
        if sumLo > 18446744073709551615:
            sumLo -= 18446744073709551616
            sumHi += 1
        if sumHi > 18446744073709551615:
            sumHi -= 18446744073709551616
        if sumLo < 0:
            sumLo = 0
        if sumHi < 0:
            sumHi = 0
        return Ip6Address(hi=sumHi, lo=sumLo)
    def __eq__(self,other):
        return self.hi == other.hi and self.lo == other.lo

class Device:
    def __init__(self, mac=0, vlan=0, ip4=0, ip4_prefix_length=0, ip4_default_gateway=0, ip6=Ip6Address(), ip6_prefix_length=0, ip6_default_gateway=Ip6Address()):
        if type(ip6) != type(Ip6Address()):
            return
        if type(ip6_default_gateway) != type(Ip6Address()):
            return
        self.mac = int(mac)
        self.vlan = int(vlan)
        self.ip4 = int(ip4)
        self.ip4_prefix_length = int(ip4_prefix_length)
        self.ip4_default_gateway = int(ip4_default_gateway)
        self.ip6 = ip6
        self.ip6_prefix_length = ip6_prefix_length
        self.ip6_default_gateway = ip6_default_gateway
        return

class NdpEntry:
    def __init__(self, ip6=Ip6Address(), mac=0):
        if type(ip6) != type(Ip6Address()):
            return
        self.ip6 = ip6
        self.mac = int(mac)
        return

class DeviceNeighborList:
    def __init__(self, device_index=0, arp=ArpEntry(), ndp=NdpEntry()):
        if type(arp) != type(ArpEntry()):
            return
        if type(ndp) != type(NdpEntry()):
            return
        self.device_index = int(device_index)
        self.arp = arp
        self.ndp = ndp
        return

class Ip4Emulation:
    def __init__(self, address=0, prefix_length=24, step=1):
        self.address = int(address)
        self.prefix_length = int(prefix_length)
        self.step = int(step)
        return

class Ip6Emulation:
    def __init__(self, address=Ip6Address(), prefix_length=64, default_gateway=Ip6Address(), step=Ip6Address(hi=0,lo=1)):
        if type(ip6) != type(Ip6Address()):
            return
        if type(ip6_default_gateway) != type(Ip6Address()):
            return
        if type(step) != type(Ip6Address()) or step == Ip6Address():
            return
        self.address = address
        self.prefix_length = int(prefix_length)
        self.default_gateway = default_gateway
        self.step = step
        return

class MacEmulation:
    def __init__(self, address=0, step=1):
        self.address = int(address)
        self.step = int(step)
        return



class Vlan:
    def __init__(self, tpid=33024, vlan_tag=100, count=1, step=1):
        self.tpid = int(tpid)
        self.vlan_tag = int(vlan_tag)
        self.count = int(count)
        self.step = int(step)
        return

class VlanEmulation:
    def __init__(self, stack=[]):
        if type(stack) != type(list()) or type(stack[0]) != type(Vlan()):
            return
        self.stack = stack
        return
    def size(self):
        return len(self.stack)
