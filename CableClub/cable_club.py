import bgb_link
from cable_club_colosseum import colosseum_process_byte
from cable_club_constants import ConnectionState, Com
from cable_club_trade_center import trade_center_process_byte


connectionState = ConnectionState.NOT_CONNECTED


def not_connected_process(byte):
    global connectionState

    if (byte == Com.MASTER):
        return Com.SLAVE
    if (byte == Com.BLANK):
        return Com.BLANK
    if (byte == Com.CONNECTED):
        connectionState = ConnectionState.CONNECTED
        return Com.CONNECTED


def connected_process(byte):
    global connectionState

    if (byte == Com.CONNECTED):
        return Com.CONNECTED
    if (byte == Com.TRADE_CENTER_SELECTED):
        connectionState = ConnectionState.TRADE_CENTER
        return Com.BLANK
    if (byte == Com.COLOSSEUM_SELECTED):
        connectionState = ConnectionState.COLOSSEUM
        return Com.BLANK
    if (byte == Com.BREAK_LINK or byte == Com.MASTER):
        connectionState = ConnectionState.NOT_CONNECTED
        return Com.BREAK_LINK

    return byte


functionSwitch = [not_connected_process, connected_process, trade_center_process_byte, colosseum_process_byte]


def cable_club_process_byte(byte):
    if (connectionState.value >= len(functionSwitch)):
        return Com.BLANK

    return functionSwitch[connectionState.value](byte)


def cable_club_begin(sim=True, address="192.168.64.2"):
    if sim:
        bgb_link.connect(8765, cable_club_process_byte, address=address)
