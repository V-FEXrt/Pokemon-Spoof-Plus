from Pokemon.pokemon_team import PokemonTeam
from Pokemon.pokemon import Pokemon

ai_team = PokemonTeam.rnd()

# Will be overwritten
enemy_team = PokemonTeam.rnd()
offered_pokemon = Pokemon.rnd()

class TradeCenter():

    @staticmethod
    def getAITeam():
        global ai_team
        return ai_team

    @staticmethod
    def recieveEnemyTeam(bytes):
        global enemy_team
        enemy_team = PokemonTeam.fromBytes(bytes)

    @staticmethod
    def offerIndex(offerByte):
        global offered_pokemon
        offered_pokemon = enemy_team.pokemon[untranslate_idx(offerByte)]
        return translate_idx(0)

    @staticmethod
    def trade_confirmed():
        global ai_team
        ai_team.trade_pokemon(0, offered_pokemon)

def translate_idx(idx):
    if idx < 0 or idx > 5:
        raise ValueError("Following must hold: 0 <= idx <= 5")
    return idx + 96

def untranslate_idx(byte):
    return  byte - 96