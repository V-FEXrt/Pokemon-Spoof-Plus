from Pokemon.pokemon_team import PokemonTeam
from Pokemon.pokemon import Pokemon

from trade_center import TradeCenter
from colosseum import Colosseum

ai_team = PokemonTeam.rnd()

# Will be overwritten
enemy_team = PokemonTeam.rnd()
offered_pokemon = Pokemon.rnd()

class TeamManager():
    trade_center = TradeCenter(ai_team, enemy_team)
    colosseum = Colosseum(ai_team, enemy_team)

    @staticmethod
    def getAITeam():
        global ai_team
        return ai_team

    @staticmethod
    def recieveEnemyTeam(bytes):
        global enemy_team
        enemy_team = PokemonTeam.fromBytes(bytes)
        TeamManager.trade_center.enemy_team = enemy_team
        TeamManager.colosseum.enemy_team = enemy_team