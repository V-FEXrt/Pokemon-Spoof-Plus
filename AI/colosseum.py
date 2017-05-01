from CableClub.cable_club_constants import Com
from Pokemon.pokemon_move import Move, MoveBase
from GameEngine.engine import process

class Colosseum():
    def __init__(self, ai_team, enemy_team):
        self.ai_team = ai_team
        self.enemy_team = enemy_team
        self.enemy_active_index = 0
        self.ai_active_index = 0

    def processTurn(self, enemy_action):
        if enemy_action >= Com.SWITCH_POKEMON_1 and enemy_action <= Com.SWITCH_POKEMON_6:
            self.enemy_active_index = enemy_action - Com.SWITCH_POKEMON_1
            print "Enemy switched to " + self.getEnemyActivePokemon().species.name

        else:
            print self.getEnemyActivePokemon().species.name + " used " + self.getEnemyActivePokemonMovedUsed(enemy_action).name


        out = self.decideAction()

        process(self.getAIActivePokemon(), self.getAIActivePokemonMovedUsed(out), self.getEnemyActivePokemon(), self.getEnemyActivePokemonMovedUsed(enemy_action))

        return out

    def getEnemyActivePokemon(self):
        return self.enemy_team.pokemon[self.enemy_active_index]

    def getEnemyActivePokemonMovedUsed(self, action):
        if action < Com.ATTACK_MOVE_1 or action > Com.ATTACK_MOVE_4:
            return Move.NOTHING

        return self.getEnemyActivePokemon().moves[action - Com.ATTACK_MOVE_1]

    def getAIActivePokemon(self):
        return self.ai_team.pokemon[self.ai_active_index]

    def getAIActivePokemonMovedUsed(self, action):
        if action < Com.ATTACK_MOVE_1 or action > Com.ATTACK_MOVE_4:
            return Move.NOTHING

        return self.getAIActivePokemon().moves[action - Com.ATTACK_MOVE_1]

    def handleResponseStateChange(self, action):
        if action >= Com.SWITCH_POKEMON_1 and action <= Com.SWITCH_POKEMON_6:
            self.ai_active_index = action - Com.SWITCH_POKEMON_1
            print "AI switched to " + self.getAIActivePokemon().species.name
        else:
            print self.getAIActivePokemon().species.name + " used " + self.getAIActivePokemonMovedUsed(action).name
        return action

    def decideAction(self):
        action = 0

        current = self.getAIActivePokemon()

        if current.currentHp.value > current.maxHp.value / 2:
            action = self.getAIDamagingMove()
        else:
            action = self.getSwitchablePokemon()

        return self.handleResponseStateChange(action)

    def getAIDamagingMove(self):
        index = 0

        for idx in range(0, len(self.getAIActivePokemon().moves)):
            if self.getAIActivePokemon().moves[idx].base is not MoveBase.STATUS:
                index = idx

        return Com.ATTACK_MOVE_1 + index

    def getSwitchablePokemon(self):
        index = 0

        for idx in range(0, len(self.ai_team.pokemon)):
            if idx == self.ai_active_index:
                continue

            consider = self.ai_team.pokemon[idx]
            if consider.currentHp.value > consider.maxHp.value / 2 :
                index = idx
                break

        return Com.SWITCH_POKEMON_1 + index

