
class TradeCenter():
    def __init__(self, ai_team, enemy_team):
        self.ai_team = ai_team
        self.enemy_team = enemy_team

    def offerIndex(self, offerByte):
        self.offered_pokemon = self.enemy_team.pokemon[untranslate_idx(offerByte)]
        return translate_idx(0)

    def trade_confirmed(self):
        self.ai_team.trade_pokemon(0, self.offered_pokemon)

def translate_idx(idx):
    if idx < 0 or idx > 5:
        raise ValueError("Following must hold: 0 <= idx <= 5")
    return idx + 96

def untranslate_idx(byte):
    return  byte - 96
