from Utilities.text_converter import *

from pokemon import Pokemon

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

def pokemon_type_block_decode(pokemon):
    pass # This can be ignored, and built from the pokemon list.. I think. It might need to be used to determine the overall length of the data

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

    def __str__(self):
        out = ""
        for p in [self.pokemon]:
            out += p.__str__() + "\n"

        return out

    def toBytes(self):
        dataBlock = []

        extend(dataBlock, trainer_name_encode(self.name))
        extend(dataBlock, pokemon_type_block_encode([self.pokemon, self.pokemon, self.pokemon, self.pokemon, self.pokemon, self.pokemon]))
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, self.pokemon.toBytes())
        extend(dataBlock, trainer_name_encode(self.pokemon.originalTrainerName)) # TODO: Must go back to set these on pokemon
        extend(dataBlock, trainer_name_encode(self.pokemon.originalTrainerName))
        extend(dataBlock, trainer_name_encode(self.pokemon.originalTrainerName))
        extend(dataBlock, trainer_name_encode(self.pokemon.originalTrainerName))
        extend(dataBlock, trainer_name_encode(self.pokemon.originalTrainerName))
        extend(dataBlock, trainer_name_encode(self.pokemon.originalTrainerName))
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())
        extend(dataBlock, self.pokemon.terminatedNickname())

        return dataBlock

    @staticmethod
    def fromBytes(bytes):
        trainer_name = trainer_name_decode(bytes[0:11])

        # Eat Type Block bytes[11:19

        pokemon1 = Pokemon.fromBytes(bytes[19:63])
        pokemon2 = Pokemon.fromBytes(bytes[63:107])
        pokemon3 = Pokemon.fromBytes(bytes[107:151])
        pokemon4 = Pokemon.fromBytes(bytes[151:195])
        pokemon5 = Pokemon.fromBytes(bytes[195:239])
        pokemon6 = Pokemon.fromBytes(bytes[239:283])

        pokemon1.originalTrainerName = trainer_name_decode(bytes[283:294])
        pokemon2.originalTrainerName = trainer_name_decode(bytes[294:305])
        pokemon3.originalTrainerName = trainer_name_decode(bytes[305:316])
        pokemon4.originalTrainerName = trainer_name_decode(bytes[316:327])
        pokemon5.originalTrainerName = trainer_name_decode(bytes[327:338])
        pokemon6.originalTrainerName = trainer_name_decode(bytes[338:349])

        pokemon1.setNickname(bytes[349:360])
        pokemon2.setNickname(bytes[360:371])
        pokemon3.setNickname(bytes[371:382])
        pokemon4.setNickname(bytes[382:393])
        pokemon5.setNickname(bytes[393:404])
        pokemon6.setNickname(bytes[404:415])

        return PokemonTeam(trainer_name, pokemon1)