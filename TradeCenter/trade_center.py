from Pokemon.pokemon_team import PokemonTeam

ai_team = PokemonTeam.rnd()

# Will be overwritten
enemy_team = PokemonTeam.rnd()

class TradeCenter():

    @staticmethod
    def getAITeam():
        return ai_team

    @staticmethod
    def recieveEnemyTeam(bytes):
        global enemy_team
        enemy_team = PokemonTeam.fromBytes(bytes)

    @staticmethod
    def offerIndex(offerByte):
        #offer = enemy_team.pokemon[untranslate_idx(offerByte)]
        return translate_idx(0)


def translate_idx(idx):
    if idx < 0 or idx > 5:
        raise ValueError("Following must hold: 0 <= idx <= 5")
    return idx + 96

def untranslate_idx(byte):
    return  byte - 96