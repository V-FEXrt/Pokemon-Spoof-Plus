from Utilities.text_converter import *

def pokemon_type_block(pokemon):
    length = len(pokemon)
    if(length > 6):
        raise ValueError("Cannot have more than 6 Pokemon")

    out = []
    out.append(hex(length))

    for i in range(6):
        if(i < length):
            out.append(hex(pokemon[i].species.hex))
        else:
            out.append("0xFF")

    out.append("0xFF")
    return  out

def trainerName(name):
    if len(name) > 7:
        raise ValueError("Name cannot be longer than 7 characters")
    return padTo(terminate(convert(name)), "0x00", 11)

def extend(bytes, arr):
    for a in arr:
        bytes.append(a)

def hex_to_int(hex_str):
    if(type(hex_str) is str):
        return int(hex_str, 16)
    return hex_str

class PokemonTeam():
    def __init__(self, pokemon):
        self.pokemon = pokemon

    def toHex(self):
        dataBlock = []

        extend(dataBlock, trainerName("HACKER"))
        extend(dataBlock, pokemon_type_block([self.pokemon, self.pokemon, self.pokemon, self.pokemon, self.pokemon, self.pokemon]))
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, trainerName(self.pokemon.originalTrainerName))
        extend(dataBlock, trainerName(self.pokemon.originalTrainerName))
        extend(dataBlock, trainerName(self.pokemon.originalTrainerName))
        extend(dataBlock, trainerName(self.pokemon.originalTrainerName))
        extend(dataBlock, trainerName(self.pokemon.originalTrainerName))
        extend(dataBlock, trainerName(self.pokemon.originalTrainerName))
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())

        return map(hex_to_int, dataBlock)
