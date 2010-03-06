TEMPLATE = app
CONFIG += qt
QT += network script
INCLUDEPATH += "../rpc/" "../common/"
LIBS += -lprotobuf
win32 {
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
    LIBS += -L"../common" -lostproto
    LIBS += -L"../rpc" -lpbrpc
    POST_TARGETDEPS += "../common/libostproto.a" "../rpc/libpbrpc.a"
}
RESOURCES += ostinato.qrc 
HEADERS += \
    dumpview.h \
    hexlineedit.h \
    mainwindow.h \
    packetmodel.h \
    port.h \
    portgroup.h \
    portgrouplist.h \
    portmodel.h \
    portstatsmodel.h \
    portstatsfilterdialog.h \
    portstatswindow.h \
    portswindow.h \
    streamconfigdialog.h \
    streamlistdelegate.h \
    streammodel.h 

FORMS += \
    about.ui \
    mainwindow.ui \
    portstatsfilter.ui \
    portstatswindow.ui \
    portswindow.ui \
    streamconfigdialog.ui 

SOURCES += \
    dumpview.cpp \
    stream.cpp \
    hexlineedit.cpp \
    main.cpp \
    mainwindow.cpp \
    packetmodel.cpp \
    port.cpp \
    portgroup.cpp \
    portgrouplist.cpp \
    portmodel.cpp \
    portstatsmodel.cpp \
    portstatsfilterdialog.cpp \
    portstatswindow.cpp \
    portswindow.cpp \
    streamconfigdialog.cpp \
    streamlistdelegate.cpp \
    streammodel.cpp 

# TODO(LOW): Test only
include(modeltest.pri)
