# Author: Alex Winstead, awinstead2015@my.fit.edu
#Gmp class
#corrisponding .proto file :
#https://github.com/littlen101/ostinato/blob/master/common/gmp.proto

#Corrisponding API guide:
#https://apiguide.ostinato.org/module_gmp.html

class IpAddress:
    def __init__(self, v4 = 0, v6_hi = 0, v6_lo = 0):
        self.v4 = int(v4)
        self.v6_lo = int(v6_lo)
        self.v6_hi = int(v6_hi)
        return

class Gmp:
    #Class Constants
    #GroupMode
    kFixed = 0
    kIncrementGroup = 1
    kDecrementGroup = 2
    kRandomGroup = 3

    #RecordType
    kReserved = 0
    kIsInclude = 1
    kIsExclude = 2
    kToInclude = 3
    kToExclude = 4
    kAllowNew = 5
    kBlockOld = 6

    #Had to use type1 cause type is restricted pyhton name.
    def __init__(self, is_override_rsvd_code = False, type = 0,
                 rsvd_code = 0, max_response_time = 100,
                 is_override_checksum = False, checksum = 0,
                 group_address = [], group_mode = kFixed, group_count = 16,
                 group_prefix = 24, s_flag = False, qrv = 2, qqi = 125,
                 is_override_source_count = False, source_count = 0,
                 sources = [], group_records = [], is_override_group_record_count = False,
                 group_record_count = 0):
        self.type = int(type)
        self.is_override_rsvd_code = bool(is_override_rsvd_code)
        self.rsvd_code = int(rsvd_code)
        self.max_response_time = int(max_response_time)
        self.is_override_checksum = bool(is_override_checksum)
        self.checksum = int(checksum)
        self.group_address = IpAddress(group_address)
        self.group_mode = int(group_mode)
        self.group_count = int(group_count)
        self.group_prefix = int(group_prefix)
        self.s_flag = bool(s_flag)
        self.qrv = int(qrv)
        self.qqi = int(qqi)
        self.sources = List[IpAddress](sources)
        self.is_override_source_count = bool(is_override_source_count)
        self.source_count = int(source_count)
        self.group_records = List[GroupRecord](group_records)
        self.is_override_group_record_count = bool(is_override_group_record_count)
        self.group_record_count = int(group_record_count)
        return

class GroupRecord:
    def __init__(self, type = Gmp.kIsInclude, group_address = IpAddress(),
                     sources = [], is_override_source_count = False,
                     source_count = 0,aux_data = "",
                     is_override_aux_data_length = False,
                     aux_data_length = 0, 
                     ):
        self.type = RecordType(type)
        self.group_address = IpAddress(group_address)
        self.sources = List[IpAddress](sources)
        self.is_override_source_count = bool(is_override_source_count)
        self.source_count = int(source_count)
        self.aux_data = str(aux_data)
        self.is_override_aux_data_length = bool(is_override_aux_data_length)
        self.aux_data_length = int(aux_data_length)
        return
