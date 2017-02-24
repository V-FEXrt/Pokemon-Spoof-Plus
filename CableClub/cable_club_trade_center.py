from cable_club_constants import TradeCenterState, Com

tradeCenterState = TradeCenterState.INIT
counter = 0
eat_byte = False
ate_byte = 0x0

DATA_BLOCK = []
RESP_BLOCK = []

def set_data_block(bytes):
    global DATA_BLOCK
    DATA_BLOCK = bytes


def init_process(byte):
    global counter, tradeCenterState

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
        resp_blok.append(byte)
        return DATA_BLOCK[counter - 1]

    return byte


def start_sending_data_process(byte):
    return byte


def sending_data_process(byte):
    global counter, tradeCenterState

    send = DATA_BLOCK[counter]
    resp_blok.append(byte)
    counter += 1
    if (counter == len(DATA_BLOCK)):
        tradeCenterState = TradeCenterState.CHOOSING_TRADE
        print "-------Begin Resp Block-------"
        print resp_blok
        print "--------End Resp Block--------"
    return send


def choosing_trade_process(byte):
    global counter, tradeCenterState, eat_byte

    if byte == 96 and counter > 0:
        counter = 0
        return byte

    if byte >= 96 and byte <= 101:
        eat_byte = True
        return  byte

    if eat_byte:
        tradeCenterState = TradeCenterState.CONFIRMING_TRADE
        eat_byte = False
        return byte

    return byte


def confirming_trade_process(byte):
    global tradeCenterState, eat_byte, ate_byte, counter, resp_blok
    if byte == 97 or byte == 98:
        eat_byte = True
        ate_byte = byte
        return byte

    if eat_byte:
        eat_byte = False
        if ate_byte == 97:
            tradeCenterState = TradeCenterState.CHOOSING_TRADE
            # Cancelled by partner
        if ate_byte == 98:
            tradeCenterState = TradeCenterState.INIT
            counter = 0
            resp_blok = []
            # Confirmed by partner

    return  byte

functionSwitch = [init_process, ready_to_go_process, seen_first_wait_process, sending_random_data_process,
                  waiting_to_send_data_process, start_sending_data_process, sending_data_process, choosing_trade_process, confirming_trade_process]


def trade_center_process_byte(byte):
    if (tradeCenterState.value >= len(functionSwitch)):
        print "Warning: no function for Trade Center State"
        return byte

    return functionSwitch[tradeCenterState.value](byte)
