import bgb_link

from cable_club_constants import ConnectionState, Com
from cable_club_initial_data_transfer import init_data_transfer_byte, set_center_or_trade


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
        set_center_or_trade(True)
        return Com.BLANK
    if (byte == Com.COLOSSEUM_SELECTED):
        connectionState = ConnectionState.COLOSSEUM
        set_center_or_trade(False)
        return Com.BLANK
    if (byte == Com.BREAK_LINK or byte == Com.MASTER):
        connectionState = ConnectionState.NOT_CONNECTED
        return Com.BREAK_LINK

    return byte


functionSwitch = [not_connected_process, connected_process, init_data_transfer_byte, init_data_transfer_byte]

def cable_club_process_byte(byte):
    if (connectionState >= len(functionSwitch)):
        return Com.BLANK

    return functionSwitch[connectionState](byte)


def cable_club_begin(sim=True, address="192.168.64.2"):
    if sim:
        bgb_link.connect(8765, cable_club_process_byte, address="192.168.0.19") #
