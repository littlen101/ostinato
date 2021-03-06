# Author: Nick Lewis, nlewis2016@my.fit.edu
# protocol_pb2.py
# Shortened as 'ost_pb'

# Reference material protocol.proto

# API guide: https://apiguide.ostinato.org/module_ost_pb.html
import emulproto_pb2_py as emul

# enum
class LinkState:
    # Module Constants
    # LinkState - Constants
    # Determine whether a connection has been made
    LinkStateUnknown = 0
    LinkStateDown = 1
    LinkStateUp = 2
# enum
class NotifType:
    # NotifType - Constants
    # Check whether a port configuration has changed
    portConfigChanged = 1
# enum
class TransmitMode:
    # Determine which Transmit Mode to use
    # Sequential Transmission - Sort higher priority packets in packet list
    kSequentialTransmit = 0
    # Interleaved Transmission - Standard fragmented packet storage - No sorting is done
    # Default
    kInterleavedTransmit = 1

def __init__ (self):
   pass


class Ack:
    # In protocol.proto there is no implementation of Ack
    # in CPP side -- python can't interact with it
    def __init__(self):
        pass

class CaptureBuffer:
    # In protocol.proto there is no implementation of CaptureBuffer
    # in CPP side -- python can't interact with it
    def __init__(self):
        pass

class CaptureBufferList:
    # List of CaptureBuffer
    def __init__(self):
        self.list = [] #find it odd they have a CaptureBufferList but no CaptureBuffer

    def appendCaptureBuffer (self, captureBuffer):
        self.list.append(captureBuffer)


class DeviceGroup:
    # The targets that will be receiving test packets
    def __init__(self,devicegroupid, devicegroupcore, encapemulation, devicecount = 1):
        # DeviceGroupId object
        self.device_group_id = devicegroupid
        # Device manager core
        self.core = devicegroupcore
        # Protocol Emulation
        self.encap = encapemulation
        # How many devices are in the group
        self.device_count = devicecount
        # Available Extensions
        self.Extensions = {
            'ip4': emul.Ip4Emulation,
            'ip6' : emul.Ip6Emulation,
            'mac' : emul.MacEmulation,
        }

class DeviceGroupConfigList:
    def __init__(self, portid):
        # PortId object
        self.port_id = portid
        # list of DeviceGroup to configure
        self.device_group = []
    # Add a DeviceGroup to list to be configured
    def appendDeviceGroup (self, devicegroup):
        self.device_group.append(devicegroup)

class DeviceGroupCore:
    # Names a DeviceGroup
    def __init__(self, name =""):
        self.name = name

class DeviceGroupId:
    # Unique id to device group
    def __init__(self, id):
        self.id = id


class DeviceGroupIdList:
    # List of DeviceGroupId
    def __init__(self, portid):
        self.port_id = portid
        self.device_group_id = []
    # Add a DeviceGroupId to list
    def appendDeviceGroup (self, devicegroupid):
        self.device_group_id.append(devicegroupid)

class EncapEmulation:
    def __init__(self):
        self.Extensions = {
            "vlan" : emul.VlanEmulation,
        }

class Notification:
    def __init__(self, notiftype, portidlist):
        self.notif_type = notiftype
        self.port_id_list = portidlist

class Port:
    def __init__(self, portid, name="", description="", notes="", is_enabled=False, is_exclusive_control=False,
                transmitmode = TransmitMode.kSequentialTransmit, username="", is_tracking_stream_stats=False):

        self.port_id = portid
        self.name = name
        self.description = description
        self.notes = notes
        self.is_enabled = is_enabled
        self.is_exclusive_control = is_exclusive_control
        # Default transmit mode = Sequential
        self.transmit_mode = transmitmode
        self.user_name = username
        self.is_tracking_stream_stats = is_tracking_stream_stats

class PortDeviceList:
    def __init__(self, portid):
        self.port_id = portid
        self.Extensions = {
            "device" : emul.Device,
        }

class PortId:
    def __init__(self, id):
        self.id = id

class PortIdList:
    def __init__(self):
        self.port_id = []
    # Add a PortId to list
    def appendPortId (self, portid):
        self.port_id.append(portid)

class PortNeighborList:
    def __init__(self, portid):
        self.port_id = PortId
        self.Extensions = {
            "device_neighbor" : emul.DeviceNeighborList,
        }

class PortState:
    def __init__(self, linkstate = LinkState.LinkStateUnknown, is_transmit_on = False, is_capture_on = False):
        self.link_state = linkstate
        self.is_transmit_on = is_transmit_on
        self.is_capture_on = is_capture_on

class PortStats:
    def __init__(self, portid, portstate, rx_pkts=0, rx_bytes=0, rx_pkts_nic=0, rx_bytes_nic=0, rx_pps=0, rx_bps=0,
                 tx_pkts=0, tx_bytes=0, tx_pkts_nic=0, tx_pps=0, tx_bps=0, rx_drops=0, rx_errors=0, rx_fifo_errors=0,
                 rx_frame_error=0):
        self.portid = portid
        self.state =  portstate
        self.rx_pkts = rx_pkts
        self.rx_bytes = rx_bytes
        self.rx_pkts_nic = rx_pkts_nic
        self.rx_bytes_nic = rx_bytes_nic
        self.rx_pps = rx_pps
        self.rx_bps = rx_bps
        self.tx_pkts = tx_pkts
        self.tx_bytes = tx_bytes
        self.tx_pkts_nic = tx_pkts_nic
        self.tx_pps = tx_pps
        self.tx_bps = tx_bps
        self.rx_drops = rx_drops
        self.rx_errors = rx_errors
        self.rx_fifo_errors = rx_fifo_errors
        self.rx_frame_error = rx_frame_error

class PortStatsList:
    def __init__(self):
        # List of Port Stats
        self.port_stats = []
    # Add a PortStat to list
    def appendPortStat (self, portstat):
        self.port_stats.append(portstat)

class Protocol:
    class k :
        kMacFieldNumber = 0
        kPayloadFieldNumber = 0
        kSampleFieldNumber = 0
        kUserScriptFieldNumber = 0
        kHexDumpFieldNumber = 0
        kSignFieldNumber = 0
        kEth2FieldNumber = 0
        kDot3FieldNumber = 0
        kLlcFieldNumber = 0
        kSnapFieldNumber = 0
        kSvlanFieldNumber = 0
        kVlanFieldNumber = 0
        kDot2LlcFieldNumber = 0
        kDot2SnapFieldNumber = 0
        kVlanStackFieldNumber = 0
        kStpFieldNumber = 0
        kArpFieldNumber = 0
        kIp4FieldNumber = 0
        kIp6FieldNumber = 0
        kIp6over4FieldNumber = 0
        kIp4over6FieldNumber = 0
        kIp4over4FieldNumber = 0
        kIp6over6FieldNumber = 0
        kTcpFieldNumber = 0
        kUdpFieldNumber = 0
        kIcmpFieldNumber = 0
        kIgmpFieldNumber = 0
        kMldFieldNumber = 0
        kTextProtocolFieldNumber = 0

    def __init__(self, protocolid):
        self.protocol_id = protocolid
        self.variable_field = []
    # Add a VariableField to list
    def appendVariableField (self, variablefield):
        self.variable_field.append(variablefield)

class Protocolid:
    def __init__(self, id):
        self.id =  id

class Stream:
    def __init__(self, id, core=None, control=None):
        self.id = id
        self.core = core
        self.control = control
        self.protocol = []

    # Add a Protocol to list
    def appendProtocol (self, protocol):
        self.protocol.append(protocol)

class StreamConfigList:
    def __init__(self, portid):
        self.port_id = portid
        self.stream = []
    # Add a Stream to list of Streams to config
    def appendStream (self, stream):
        self.stream.append(stream)

class StreamControl:
    class NextWhat:
        e_nw_stop = 0
        e_nw_goto_next = 1
        e_nw_goto_id = 2

    class SendMode:
        e_sm_fixed = 0
        e_sm_continuous = 1

    class SendUnit:
        e_su_packets = 0
        e_su_bursts = 1

    def __init__(self, unit=SendUnit.e_su_packets, mode=SendMode.e_sm_fixed, num_packets=10, num_bursts=1,
                 packets_per_burt=10, next=NextWhat.e_nw_goto_next, OBSOLETE_packets_per_sec=1,
                 OBSOLETE_bursts_per_sec = 1, packets_per_sec=1, bursts_per_sec=1):
        self.unit = unit
        self.mode = mode
        self.num_packets = num_packets
        self.num_bursts = num_bursts
        self.packets_per_burst = packets_per_burt
        self.next = next
        self.OBSOLETE_packets_per_sec = OBSOLETE_packets_per_sec
        self.OBSOLETE_bursts_per_sec = OBSOLETE_bursts_per_sec
        self.packets_per_sec = packets_per_sec
        self.bursts_per_sec = bursts_per_sec


class StreamCore:
    class FrameLengthMode:
        e_fl_fixed = 0
        e_fl_inc = 1
        e_fl_dec = 2
        e_fl_random = 3

    def __init__(self, name="", is_enabled=False, ordinal=0, len_mode=FrameLengthMode.e_fl_fixed, frame_len=64,
                 frame_len_min=64, frame_len_max=1518):
        self.name = name
        self.is_enabled = is_enabled
        self.ordinal = ordinal
        self.len_mode = len_mode
        self.frame_len = frame_len
        self.frame_len_min = frame_len_min
        self.frame_len_max = frame_len_max



class StreamGuidList:
    def __init__(self, portidlist):
        self.port_id_list = portidlist
        self.stream_guid = []
    # Add a Stream to list
    def appendStreamGuid (self, streamguid):
        self.stream_guid.append(streamguid)

class StreamGuid:
    def __init__(self, id):
        self.id = id

class StreamId:
    def __init__(self, id):
        self.id = id

class StreamIdList:
    def __init__(self, portid):
        self.port_id = portid
        self.stream_id = []
    # Add a StreamId to list
    def appendStreamId (self, streamid):
        self.stream_id.append(streamid)

class StreamStats:
    def __init__(self, portid, streamguid, rx_pkts=0, rx_bytes=0, tx_pkts=0, tx_bytes=0):
        self.port_id = portid
        self.stream_guid =  streamguid
        self.rx_pkts = rx_pkts
        self.rx_bytes =  rx_bytes
        self.tx_pkts = tx_pkts
        self.tx_bytes = tx_bytes

class StreamStatsList:
    def __init__(self):
        self.stream_stats = []
    # Add a StreamStat to list
    def appendStreamStat (self, streamstat):
        self.stream_stats.append(streamstat)

class VariableField:
    class Mode:
        kIncrement = 0
        kDecrement = 1
        kRandom = 2

    class Type:
        kCounter8 = 0
        kCounter16 = 1
        kCounter32 = 2

    def __init__(self, type=Type.kCounter8, offset=0, mask=4294967295, value=0, mode=Mode.kIncrement, count=16, step=1):
        self.type = type
        self.offset = offset
        self.mask = mask
        self.value = value
        self.mode = mode
        self.count = count
        self.step = step

class VersionCompatibility:
    class Compatibility:
        kIncompatible = 0
        kCompatible =  1

    def __init__(self, result, notes=""):
        self.result = result
        self.notes = notes


class VersionInfo:
    def __init__(self, version, client_name=""):
        self.version = version
        self.client_name = client_name


class Void:
    # Nothing!
    def __init__(self):
        pass
