from CableClub.cable_club_constants import Com

class Colosseum():
    def __init__(self, ai_team, enemy_team):
        self.ai_team = ai_team
        self.enemy_team = enemy_team
        self.active_index = 0

    def processTurn(self, enemy_action):
        if enemy_action >= Com.SWITCH_POKEMON_1 and enemy_action <= Com.SWITCH_POKEMON_6:
            self.active_index = enemy_action - Com.SWITCH_POKEMON_1
            print "Enemy switched to " + self.getActivePokemon().species.name

        else:
            print self.getActivePokemon().species.name + " used " + self.getActivePokemonMovedUsed(enemy_action).name


        return Com.ATTACK_MOVE_1

    def getActivePokemon(self):
        return self.enemy_team.pokemon[self.active_index]

    def getActivePokemonMovedUsed(self, action):
        return self.getActivePokemon().moves[action - Com.ATTACK_MOVE_1]