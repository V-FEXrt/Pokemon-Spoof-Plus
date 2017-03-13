from cable_club_constants import TradeCenterState, Com
from TradeCenter.trade_center import TradeCenter

tradeCenterState = TradeCenterState.INIT
counter = 0
eat_byte = False
ate_byte = 0x0
is_init = False

DATA_BLOCK = []
RESP_BLOCK = []

choice_byte = 0

def init_process(byte):
    global counter, tradeCenterState, DATA_BLOCK, is_init

    if not is_init:
        is_init = True
        DATA_BLOCK = TradeCenter.getAITeam().toBytes()

    if (byte == Com.BLANK):
        if (counter == 5):
            tradeCenterState = TradeCenterState.READY_TO_GO
        counter += 1
    return byte


def ready_to_go_process(byte):
    global tradeCenterState

    if ((byte & Com.WAIT) == Com.WAIT):
        tradeCenterState = TradeCenterState.SEEN_FIRST_WAIT
    return byte


def seen_first_wait_process(byte):
    global counter, tradeCenterState

    if ((byte & Com.WAIT) != Com.WAIT):
        counter = 0
        tradeCenterState = TradeCenterState.SENDING_RANDOM_DATA
    return byte


def sending_random_data_process(byte):
    global counter, tradeCenterState

    if ((byte & Com.WAIT) == Com.WAIT):
        if (counter == 5):
            tradeCenterState = TradeCenterState.WAITING_TO_SEND_DATA
        counter += 1
    return byte


def waiting_to_send_data_process(byte):
    global counter, tradeCenterState

    if ((byte & Com.WAIT) != Com.WAIT):
        counter = 0
        tradeCenterState = TradeCenterState.SENDING_DATA
        counter += 1
        RESP_BLOCK.append(byte)
        return DATA_BLOCK[counter - 1]

    return byte


def start_sending_data_process(byte):
    return byte


def sending_data_process(byte):
    global counter, tradeCenterState

    send = DATA_BLOCK[counter]
    RESP_BLOCK.append(byte)
    counter += 1
    if (counter == len(DATA_BLOCK)):
        tradeCenterState = TradeCenterState.CHOOSING_TRADE
        TradeCenter.recieveEnemyTeam(RESP_BLOCK)

    return send


def choosing_trade_process(byte):
    global counter, tradeCenterState, eat_byte, choice_byte

    ## Eat 'random' 96 byte
    if byte == 96 and counter > 0:
        counter = 0
        return byte

    if byte >= 96 and byte <= 101:
        # TODO: 'seen first wait' solves this eating bytes problem better. Should use it instead
        if not eat_byte:
            choice_byte = TradeCenter.offerIndex(byte)

        eat_byte = True
        return  choice_byte

    if eat_byte:
        tradeCenterState = TradeCenterState.CONFIRMING_TRADE
        eat_byte = False
        return byte

    return byte


def confirming_trade_process(byte):
    global tradeCenterState, eat_byte, ate_byte, counter, RESP_BLOCK, is_init
    if byte == 97 or byte == 98:
        eat_byte = True
        ate_byte = byte
        return byte

    if eat_byte:
        eat_byte = False
        if ate_byte == 97:
            # Cancelled by partner
            tradeCenterState = TradeCenterState.CHOOSING_TRADE
        if ate_byte == 98:
            # Confirmed by partner
            tradeCenterState = TradeCenterState.INIT
            counter = 0
            RESP_BLOCK = []
            is_init = False
            TradeCenter.trade_confirmed()


    return  byte

functionSwitch = [init_process, ready_to_go_process, seen_first_wait_process, sending_random_data_process,
                  waiting_to_send_data_process, start_sending_data_process, sending_data_process, choosing_trade_process, confirming_trade_process]

def trade_center_process_byte(byte):
    if (tradeCenterState >= len(functionSwitch)):
        print "Warning: no function for Trade Center State"
        return byte

    return functionSwitch[tradeCenterState](byte)

