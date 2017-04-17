from Folder.team_manager import TeamManager
from CableClub.cable_club_constants import Com
def colosseum_process_byte(byte):
    if byte >= Com.ATTACK_MOVE_1 and byte <= Com.SWITCH_POKEMON_6:
        out = TeamManager.colosseum.processTurn(byte)
        print "(" + str(byte) + ", " + str(out) + ") - CL"
        return out
    print "(" + str(byte) + ", " + str(byte) + ") - PB"
    return byte