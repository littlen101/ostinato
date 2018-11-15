/*
Copyright (C) 2015 Srivats P.

This file is part of "Ostinato"

This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
*/

#ifndef _DEVICE_H
#define _DEVICE_H

#include "../common/emulproto.pb.h"
#include "../common/protocol.pb.h"
#include "../common/uint128.h"

#include <QByteArray>
#include <QHash>
#include <QString>

class DeviceManager;
class PacketBuffer;

class DeviceKey: public QByteArray
{
};

class Device
{
public:
    static const quint16 kVlanTpid = 0x8100;

    enum NeighborSet {
        kAllNeighbors,
        kUnresolvedNeighbors
    };

public:
    Device(DeviceManager *deviceManager);

    void setVlan(int index, quint16 vlan, quint16 tpid = kVlanTpid);
    quint64 mac();
    void setMac(quint64 mac);
    void setIp4(quint32 address, int prefixLength, quint32 gateway);
    void setIp6(UInt128 address, int prefixLength, UInt128 gateway);
    void getConfig(OstEmul::Device *deviceConfig);
    QString config();

    DeviceKey key();
    void clearKey();

    int encapSize();
    void encap(PacketBuffer *pktBuf, quint64 dstMac, quint16 type);

    void receivePacket(PacketBuffer *pktBuf);
    void transmitPacket(PacketBuffer *pktBuf);

    void resolveGateway();

    void clearNeighbors(Device::NeighborSet set);
    void resolveNeighbor(PacketBuffer *pktBuf);
    void getNeighbors(OstEmul::DeviceNeighborList *neighbors);

    bool isOrigin(const PacketBuffer *pktBuf);
    quint64 neighborMac(const PacketBuffer *pktBuf);

private: // methods
    void receiveArp(PacketBuffer *pktBuf);
    void sendArpRequest(PacketBuffer *pktBuf);
    void sendArpRequest(quint32 tgtIp);

    void receiveIp4(PacketBuffer *pktBuf);
    void sendIp4Reply(PacketBuffer *pktBuf);

    void receiveIcmp4(PacketBuffer *pktBuf);

    void receiveIp6(PacketBuffer *pktBuf);
    bool sendIp6(PacketBuffer *pktBuf, UInt128 dstIp, quint8 protocol);
    void sendIp6Reply(PacketBuffer *pktBuf);

    void receiveIcmp6(PacketBuffer *pktBuf);

    void receiveNdp(PacketBuffer *pktBuf);
    void sendNeighborSolicit(PacketBuffer *pktBuf);
    void sendNeighborSolicit(UInt128 tgtIp);
    void sendNeighborAdvertisement(PacketBuffer *pktBuf);

private: // data
    static const int kMaxVlan = 4;

    DeviceManager *deviceManager_;

    int numVlanTags_;
    quint32 vlan_[kMaxVlan];
    quint64 mac_;

    bool hasIp4_;
    quint32 ip4_;
    int ip4PrefixLength_;
    quint32 ip4Gateway_;
    quint32 ip4Mask_;
    quint32 ip4Subnet_;

    bool hasIp6_;
    UInt128 ip6_;
    int ip6PrefixLength_;
    UInt128 ip6Gateway_;
    UInt128 ip6Mask_;
    UInt128 ip6Subnet_;

    DeviceKey key_;

    QHash<quint32, quint64> arpTable_;
    QHash<UInt128, quint64> ndpTable_;
};

bool operator<(const DeviceKey &a1, const DeviceKey &a2);
#endif

