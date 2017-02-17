import Utilities
from CableClub.cable_club import cable_club_begin
from Pokemon.pokemon_team import PokemonTeam
from Pokemon.pokemon_species import Species
from Pokemon.pokemon_item import Item
from Pokemon.pokemon_move import Move
from Pokemon.pokemon_type import Type
from Pokemon.status_ailment import  StatusAilment
from Pokemon.pokemon import Pokemon


team = PokemonTeam.rnd()

#print PokemonTeam.fromBytes(team.toBytes())
cable_club_begin(team.toBytes())

# TODO: Add abilty to select which pokemon the program trades
# TODO: Resend new team after completed trade
# TODO: Need a trade center event handler that is passed to cable club

# Notes
## Resp Block with some pokemon no nickname
from_emu = [128, 146, 135, 80, 0, 0, 0, 0, 0, 0, 0, 5, 180, 165, 165, 36, 165, 255, 0, 180, 1, 18, 74, 0, 20, 8, 31, 126, 56, 9, 25, 4, 210, 3, 13, 64, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 192, 192, 192, 192, 74, 1, 44, 0, 150, 0, 151, 0, 152, 0, 153, 165, 0, 15, 0, 0, 0, 0, 255, 33, 39, 0, 0, 148, 213, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 197, 203, 35, 30, 0, 0, 3, 0, 15, 0, 9, 0, 7, 0, 10, 0, 7, 165, 0, 15, 0, 0, 0, 0, 255, 33, 39, 0, 0, 148, 213, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57, 199, 35, 30, 0, 0, 3, 0, 15, 0, 8, 0, 7, 0, 10, 0, 6, 36, 0, 15, 0, 0, 0, 2, 255, 16, 0, 0, 0, 148, 213, 0, 0, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 199, 121, 35, 0, 0, 0, 3, 0, 15, 0, 8, 0, 7, 0, 8, 0, 7, 165, 0, 15, 0, 0, 0, 0, 255, 33, 39, 0, 0, 148, 213, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 118, 235, 35, 30, 0, 0, 3, 0, 15, 0, 8, 0, 7, 0, 10, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 129, 142, 129, 129, 142, 80, 0, 0, 0, 0, 0, 128, 146, 135, 80, 0, 0, 0, 0, 0, 0, 0, 128, 146, 135, 80, 0, 0, 0, 0, 0, 0, 0, 128, 146, 135, 80, 0, 0, 0, 0, 0, 0, 0, 128, 146, 135, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 171, 162, 167, 164, 172, 184, 80, 80, 80, 80, 145, 128, 147, 147, 128, 147, 128, 80, 80, 80, 80, 145, 128, 147, 147, 128, 147, 128, 80, 80, 80, 80, 143, 136, 131, 134, 132, 152, 80, 80, 80, 80, 80, 145, 128, 147, 147, 128, 147, 128, 80, 80, 80, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## 97 means trade second pokemon