import Utilities
from CableClub.cable_club import cable_club_begin
from Pokemon.pokemon_team import PokemonTeam
from Pokemon.pokemon_species import Species
from Pokemon.pokemon_item import Item
from Pokemon.pokemon_move import Move
from Pokemon.pokemon_type import Type
from Pokemon.status_ailment import  StatusAilment
from Pokemon.pokemon import Pokemon

pokemon = Pokemon(
    Species.CHARIZARD,
    300,
    74,
    StatusAilment.NONE,
    Type.FIRE,
    Type.GHOST,
    Item.CALCIUM,
    Move.FIRE_BLAST,
    Move.HYDRO_PUMP,
    Move.THUNDER_PUNCH,
    Move.MEGA_KICK,
    1234,
    200000,
    65535,
    65535,
    65535,
    65535,
    65535,
    65535,
    3 << 6,
    3 << 6,
    3 << 6,
    3 << 6,
    74,
    300,
    150,
    151,
    152,
    153,
    "Alchemy",
    "BOBBO")

team = PokemonTeam(pokemon)


cable_club_begin(team.toHex())