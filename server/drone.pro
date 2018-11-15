TEMPLATE = app
CONFIG += qt ver_info
QT += network script xml
QT -= gui
linux*:system(grep -q IFLA_STATS64 /usr/include/linux/if_link.h): \
    DEFINES += HAVE_IFLA_STATS64
INCLUDEPATH += "../rpc"
win32 {
    DEFINES += HAVE_REMOTE WPCAP
    CONFIG += console
    QMAKE_LFLAGS += -static
    LIBS += -lwpcap -lpacket
    CONFIG(debug, debug|release) {
        LIBS += -L"../common/debug" -lostproto
        LIBS += -L"../rpc/debug" -lpbrpc
        POST_TARGETDEPS += \
            "../common/debug/libostproto.a" \
            "../rpc/debug/libpbrpc.a"
    } else {
        LIBS += -L"../common/release" -lostproto
        LIBS += -L"../rpc/release" -lpbrpc
        POST_TARGETDEPS += \
            "../common/release/libostproto.a" \
            "../rpc/release/libpbrpc.a"
    }
} else {
    LIBS += -lpcap
    LIBS += -L"../common" -lostproto
    LIBS += -L"../rpc" -lpbrpc
    POST_TARGETDEPS += "../common/libostproto.a" "../rpc/libpbrpc.a"
}
LIBS += -lm
LIBS += -lprotobuf
HEADERS += drone.h \
    pcaptransmitter.h \
    myservice.h
SOURCES += \
    devicemanager.cpp \
    device.cpp \
    drone_main.cpp \
    drone.cpp \
    portmanager.cpp \
    abstractport.cpp \
    pcapport.cpp \
    pcaptransmitter.cpp \
    pcaprxstats.cpp \
    pcaptxstats.cpp \
    pcaptxthread.cpp \
    bsdport.cpp \
    linuxport.cpp \
    winpcapport.cpp 
SOURCES += myservice.cpp 
SOURCES += pcapextra.cpp 
SOURCES += packetbuffer.cpp

QMAKE_DISTCLEAN += object_script.*

include (../install.pri)
include (../version.pri)
include (../options.pri)
