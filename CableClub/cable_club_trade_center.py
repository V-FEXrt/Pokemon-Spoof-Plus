from cable_club_constants import TradeCenterState, Com

tradeCenterState = TradeCenterState.INIT
counter = 0

DATA_BLOCK = []

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
        return DATA_BLOCK[counter - 1]

    return byte


def start_sending_data_process(byte):
    return byte


def sending_data_process(byte):
    global counter, tradeCenterState

    send = DATA_BLOCK[counter]
    counter += 1
    if (counter == len(DATA_BLOCK)):
        tradeCenterState = TradeCenterState.DATA_SENT
    return send


def data_sent_process(byte):
    return byte


functionSwitch = [init_process, ready_to_go_process, seen_first_wait_process, sending_random_data_process,
                  waiting_to_send_data_process, start_sending_data_process, sending_data_process, data_sent_process]


def trade_center_process_byte(byte):
    if (tradeCenterState.value >= len(functionSwitch)):
        return byte

    return functionSwitch[tradeCenterState.value](byte)
