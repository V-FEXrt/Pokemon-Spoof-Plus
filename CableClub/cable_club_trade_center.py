from AI.team_manager import TeamManager
from cable_club_constants import TradeCenterState, Com

def reset():
    global tradeCenterState, counter, eat_byte, ate_byte, choice_byte
    tradeCenterState = TradeCenterState.CHOOSING_TRADE
    counter = 416
    eat_byte = False
    ate_byte = 0x0
    choice_byte = 0

reset()

def set_reset_callback(func):
    global reset_to_init
    reset_to_init = func

def choosing_trade_process(byte):
    global counter, tradeCenterState, eat_byte, choice_byte

    ## Eat 'random' 96 byte
    if byte == 96 and counter > 0:
        counter = 0
        return byte

    if byte >= 96 and byte <= 101:
        # TODO: 'seen first wait' solves this eating bytes problem better. Should use it instead
        if not eat_byte:
            choice_byte = TeamManager.trade_center.offerIndex(byte)

        eat_byte = True
        return  choice_byte

    if eat_byte:
        tradeCenterState = TradeCenterState.CONFIRMING_TRADE
        eat_byte = False
        return byte

    return byte


def confirming_trade_process(byte):
    global tradeCenterState, eat_byte, ate_byte, counter
    if byte == 97 or byte == 98:
        eat_byte = True
        ate_byte = byte
        return byte

    if eat_byte:
        eat_byte = False
        if ate_byte == 97:
            # Cancelled by partner
            tradeCenterState = TradeCenterState.CHOOSING_TRADE
            print "Trade cancelled by Player"
        if ate_byte == 98:
            # Confirmed by partner
            print "Trade confirmed by Player"
            reset_to_init()
            reset()
            TeamManager.trade_center.trade_confirmed()


    return  byte

functionSwitch = [choosing_trade_process, confirming_trade_process]

def trade_center_process_byte(byte):
    if (tradeCenterState >= len(functionSwitch)):
        print "Warning: no function for Trade Center State"
        return byte

    return functionSwitch[tradeCenterState](byte)

