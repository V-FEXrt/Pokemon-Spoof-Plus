import random

from Utilities.text_converter import *

from pokemon import Pokemon
from pokemon_species import Species

def pokemon_type_block_encode(pokemon):
    length = len(pokemon)
    if(length > 6):
        raise ValueError("Cannot have more than 6 Pokemon")

    out = []
    out.append(length)

    for i in range(6):
        if(i < length):
            out.append(pokemon[i].species.hex)
        else:
            out.append(0xFF)

    out.append(0xFF)

    return  out

def pokemon_type_block_decode(bytes):
    pokemon_count = bytes[0]
    species = []
    for i in range(pokemon_count):
        species.append(Species.fromBytes(bytes[i+1]))

    return  [pokemon_count, species]

def trainer_name_encode(name):
    if len(name) > 7:
        raise ValueError("Name cannot be longer than 7 characters")
    return padTo(terminate(encode(name)), 0x00, 11)

def trainer_name_decode(bytes):
    if len(bytes) is not 11:
        print "Warning trainer name data should be 11 bytes"
    return decode(unterminate(removePad(bytes, 0)))

def extend(bytes, arr):
    for a in arr:
        bytes.append(a)

class PokemonTeam():
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon

        if len(name) > 7:
            raise ValueError("Name cannot be longer than 7 characters")

        if len(pokemon) > 6:
            raise ValueError("Cannot have more than 6 Pokemon")

    def __str__(self):
        out = ""
        for p in self.pokemon:
            out += p.__str__() + "\n"

        return out

    def toBytes(self):
        dataBlock = []

        extend(dataBlock, trainer_name_encode(self.name))
        extend(dataBlock, pokemon_type_block_encode(self.pokemon))

        length = len(self.pokemon)
        for i in range(6):
            if (i < length):
                extend(dataBlock, self.pokemon[i].toBytes())
            else:
                # Fill with 0 bytes
                extend(dataBlock, padTo([], 0x00, 44))

        for i in range(6):
            if (i < length):
                extend(dataBlock, trainer_name_encode(self.pokemon[i].originalTrainerName))
            else:
                # Fill with 0 bytes
                extend(dataBlock, padTo([], 0x00, 11))

        for i in range(6):
            if (i < length):
                extend(dataBlock, self.pokemon[i].terminatedNickname())
            else:
                # Fill with 0 bytes
                extend(dataBlock, padTo([], 0x00, 11))

        return dataBlock

    @staticmethod
    def fromBytes(bytes):
        trainer_name = trainer_name_decode(bytes[0:11])

        meta = pokemon_type_block_decode(bytes[11:19])

        pokemon = []

        byte_idx = 19
        for i in range(meta[0]):
            pokemon.append(Pokemon.fromBytes(bytes[byte_idx:byte_idx+44]))
            byte_idx += 44

        byte_idx = 283
        for i in range(meta[0]):
            pokemon[i].originalTrainerName = trainer_name_decode(bytes[byte_idx:byte_idx+11])
            byte_idx += 11

        byte_idx = 349
        for i in range(meta[0]):
            pokemon[i].setNickname(bytes[byte_idx:byte_idx+11])
            byte_idx += 11

        return PokemonTeam(trainer_name, pokemon)

    @staticmethod
    def rnd():
        pkmn_cnt = random.randint(1, 6)
        pkmn = []
        for i in range(pkmn_cnt):
            pkmn.append(Pokemon.rnd())

        return PokemonTeam("HACKER", pkmn)
