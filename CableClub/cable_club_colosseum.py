from AI.team_manager import TeamManager
from CableClub.cable_club_constants import Com

out_byte = 0
last_recieved = 0
count = 0
def colosseum_process_byte(byte):
    global out_byte, last_recieved, count

    if byte >= Com.ATTACK_MOVE_1 and byte <= Com.SWITCH_POKEMON_6:
        if count == 12:
            last_recieved = 0

        if last_recieved == byte:
            count += 1
            return  out_byte

        count = 0
        last_recieved = byte
        out_byte = TeamManager.colosseum.processTurn(byte)
        return out_byte

    return byte