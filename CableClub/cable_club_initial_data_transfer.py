from cable_club_constants import InitDataState, Com

from cable_club_trade_center import trade_center_process_byte, set_reset_callback
from cable_club_colosseum import colosseum_process_byte

from Pokemon.pokemon_team import PokemonTeam

from Folder.team_manager import TeamManager

initDataState = InitDataState.INIT
counter = 0
eat_byte = False
ate_byte = 0x0
is_init = False

DATA_BLOCK = []
RESP_BLOCK = []

choice_byte = 0

is_trade = False

def reset_to_init():
    global initDataState, counter, RESP_BLOCK, is_init
    initDataState = InitDataState.INIT
    counter = 0
    RESP_BLOCK = []
    is_init = False

# provide reset to trade center
set_reset_callback(reset_to_init)

def init_process(byte):
    global counter, initDataState, DATA_BLOCK, is_init

    if not is_init:
        is_init = True
        DATA_BLOCK = TeamManager.getAITeam().toBytes()

    if (byte == Com.BLANK):
        if (counter == 5):
            initDataState = InitDataState.READY_TO_GO
        counter += 1
    return byte


def ready_to_go_process(byte):
    global initDataState

    if ((byte & Com.WAIT) == Com.WAIT):
        initDataState = InitDataState.SEEN_FIRST_WAIT
    return byte


def seen_first_wait_process(byte):
    global counter, initDataState

    if ((byte & Com.WAIT) != Com.WAIT):
        counter = 0
        initDataState = InitDataState.SENDING_RANDOM_DATA
    return byte


def sending_random_data_process(byte):
    global counter, initDataState

    if ((byte & Com.WAIT) == Com.WAIT):
        if (counter == 5):
            initDataState = InitDataState.WAITING_TO_SEND_DATA
        counter += 1
    return byte


def waiting_to_send_data_process(byte):
    global counter, initDataState

    if ((byte & Com.WAIT) != Com.WAIT):
        counter = 0
        initDataState = InitDataState.SENDING_DATA
        counter += 1
        RESP_BLOCK.append(byte)
        return DATA_BLOCK[counter - 1]

    return byte


def start_sending_data_process(byte):
    return byte


def sending_data_process(byte):
    global counter, initDataState

    send = DATA_BLOCK[counter]
    RESP_BLOCK.append(byte)
    counter += 1
    if (counter == len(DATA_BLOCK)):
        if is_trade:
            initDataState = InitDataState.TRADE_CENTER
        else:
            initDataState = InitDataState.COLOSSEUM
        TeamManager.recieveEnemyTeam(RESP_BLOCK)

    return send

functionSwitch = [init_process, ready_to_go_process, seen_first_wait_process, sending_random_data_process,
                  waiting_to_send_data_process, start_sending_data_process, sending_data_process, trade_center_process_byte, colosseum_process_byte]

def set_center_or_trade(p_is_trade):
    global is_trade
    is_trade = p_is_trade

def init_data_transfer_byte(byte):
    if (initDataState >= len(functionSwitch)):
        print "Warning: no function for Init Data Transfer State"
        return byte

    return functionSwitch[initDataState](byte)