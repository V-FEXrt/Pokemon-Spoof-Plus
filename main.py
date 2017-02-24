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
## 96 means trade first
## 97 means trade second pokemon
## 98 means 3rd
## 99 means 4th
## 100 5th
## 101 6th?

## 98 is also confirm
## 97 is also cancel
