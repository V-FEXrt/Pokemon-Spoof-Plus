from integer_field import IntegerField
from pokemon_item import Item
from pokemon_move import Move
from pokemon_species import Species
from pokemon_type import Type
from status_ailment import StatusAilment

from Utilities.text_converter import *

class Pokemon():
    def __init__(self, species, currentHp, levelPc, statusAilment, type1, type2, itemHeld, move1, move2, move3, move4,
                 originalTrainerId, exp, hpEv, attackEv, defenseEv, speedEv, specialEv, iv, move1pp, move2pp, move3pp,
                 move4pp, level, maxHp, attack, defense, speed, special, nickname, originalTrainerName):
        self.species = species
        self.currentHp = IntegerField(maxHp, 2)
        self.levelPc = IntegerField(levelPc, 1)
        self.statusAilment = statusAilment
        self.type1 = type1
        self.type2 = type2
        self.itemHeld = itemHeld
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.originalTrainerId = IntegerField(originalTrainerId, 2)
        self.exp = IntegerField(exp, 3)
        self.hpEv = IntegerField(hpEv, 2)
        self.attackEv = IntegerField(attackEv, 2)
        self.defenseEv = IntegerField(defenseEv, 2)
        self.speedEv = IntegerField(speedEv, 2)
        self.specialEv = IntegerField(specialEv, 2)
        self.iv = IntegerField(iv, 2)
        self.move1pp = IntegerField(move1pp, 1)
        self.move2pp = IntegerField(move2pp, 1)
        self.move3pp = IntegerField(move3pp, 1)
        self.move4pp = IntegerField(move4pp, 1)
        self.level = IntegerField(level, 1)
        self.maxHp = IntegerField(maxHp, 2)
        self.attack = IntegerField(attack, 2)
        self.defense = IntegerField(defense, 2)
        self.speed = IntegerField(speed, 2)
        self.special = IntegerField(special, 2)

        self.moves = [self.move1, self.move2, self.move3, self.move4]

        self.nickname = nickname
        if(len(nickname) > 10):
            raise ValueError("Nickname cannot be longer that 10 characters")

        self.originalTrainerName = originalTrainerName
        if(len(originalTrainerName) > 7):
            raise ValueError("Trainer name cannot be longer than 7 characters")

    def __str__(self):
        out = ""
        out += self.species.__str__() + "\n"
        out += "\tCurrent HP: " + self.currentHp.__str__() + "\n"
        out += "\tLevel PC: " + self.levelPc.__str__() + "\n"
        out += "\tStatus Ailment: " + self.statusAilment.__str__() + "\n"
        out += "\tType 1: " + self.type1.__str__() + "\n"
        out += "\tType 2: " + self.type2.__str__() + "\n"
        out += "\tItem Held: " + self.itemHeld.__str__() + "\n"
        out += "\tMove 1: " + self.move1.__str__() + "\n"
        out += "\tMove 2: " + self.move2.__str__() + "\n"
        out += "\tMove 3: " + self.move3.__str__() + "\n"
        out += "\tMove 4: " + self.move4.__str__() + "\n"
        out += "\tOriginal Trainer ID: " + self.originalTrainerId.__str__() + "\n"
        out += "\tExp: " + self.exp.__str__() + "\n"
        out += "\tHP EV: " + self.hpEv.__str__() + "\n"
        out += "\tAttack EV: " + self.attackEv.__str__() + "\n"
        out += "\tDefense EV: " + self.defenseEv.__str__() + "\n"
        out += "\tSpeed EV: " + self.speedEv.__str__() + "\n"
        out += "\tSpecial EV: " + self.specialEv.__str__() + "\n"
        out += "\tIV: " + self.iv.__str__() + "\n"
        out += "\tMove 1 PP: " + self.move1pp.__str__() + "\n"
        out += "\tMove 2 PP: " + self.move2pp.__str__() + "\n"
        out += "\tMove 3 PP: " + self.move3pp.__str__() + "\n"
        out += "\tMove 4 PP: " + self.move4pp.__str__() + "\n"
        out += "\tLevel: " + self.level.__str__() + "\n"
        out += "\tMax HP: " + self.maxHp.__str__() + "\n"
        out += "\tAttack: " + self.attack.__str__() + "\n"
        out += "\tDefense: " + self.defense.__str__() + "\n"
        out += "\tSpeed: " + self.speed.__str__() + "\n"
        out += "\tSpecial: " + self.special.__str__() + "\n"
        out += "\tNickname: " + self.nickname.__str__() + "\n"
        out += "\tOriginal Trainer Name: " + self.originalTrainerName.__str__() + "\n"

        return  out

    def terminatedNickname(self):
        return padTo(terminate(encode(self.nickname)), 0x50, 11)

    def setNickname(self, bytes):
        if len(bytes) is not 11:
            print "Warning trainer name data should be 11 bytes"

        # Don't need to unterminate here because 0x50 is the terminator
        self.nickname =  decode(removePad(bytes, 0x50))

    def extend(self, bytes, arr):
        for a in arr:
            bytes.append(a)

    def toBytes(self):
        bytes = []
        bytes.append(self.species.hex)
        self.extend(bytes, self.currentHp.toBytes())
        self.extend(bytes, self.levelPc.toBytes())
        bytes.append(self.statusAilment.hex)
        bytes.append(self.type1.hex)
        bytes.append(self.type2.hex)
        bytes.append(self.itemHeld.hex)
        bytes.append(self.move1.hex)
        bytes.append(self.move2.hex)
        bytes.append(self.move3.hex)
        bytes.append(self.move4.hex)
        self.extend(bytes, self.originalTrainerId.toBytes())
        self.extend(bytes, self.exp.toBytes())
        self.extend(bytes, self.hpEv.toBytes())
        self.extend(bytes, self.attackEv.toBytes())
        self.extend(bytes, self.defenseEv.toBytes())
        self.extend(bytes, self.speedEv.toBytes())
        self.extend(bytes, self.specialEv.toBytes())
        self.extend(bytes, self.iv.toBytes())
        self.extend(bytes, self.move1pp.toBytes())
        self.extend(bytes, self.move2pp.toBytes())
        self.extend(bytes, self.move3pp.toBytes())
        self.extend(bytes, self.move4pp.toBytes())
        self.extend(bytes, self.level.toBytes())
        self.extend(bytes, self.maxHp.toBytes())
        self.extend(bytes, self.attack.toBytes())
        self.extend(bytes, self.defense.toBytes())
        self.extend(bytes, self.speed.toBytes())
        self.extend(bytes, self.special.toBytes())
        return bytes

    @staticmethod
    def rnd():
        return Pokemon(Species.rnd(), 300, 74, StatusAilment.NONE, Type.rnd(), Type.rnd(), Item.rnd(), Move.rnd(), Move.rnd(), Move.rnd(), Move.rnd(), 1234, 200000, 65535, 65535, 65535, 65535, 65535, 65535, 3 << 6, 3 << 6, 3 << 6, 3 << 6, 74, 300, 150, 151, 152, 153, "Alchemy", "BOBBO")

    @staticmethod
    def fromBytes(bytes):
        species = Species.fromBytes(bytes[0:1][0])
        currentHp = IntegerField.fromBytes(2, bytes[1:3]).value
        levelPc = IntegerField.fromBytes(1, bytes[3:4]).value
        statusAilment = StatusAilment.fromBytes(bytes[4:5][0])
        type1 = Type.fromBytes(bytes[5:6][0])
        type2 = Type.fromBytes(bytes[6:7][0])
        itemHeld = Item.fromBytes(bytes[7:8][0])
        move1 = Move.fromBytes(bytes[8:9][0])
        move2 = Move.fromBytes(bytes[9:10][0])
        move3 = Move.fromBytes(bytes[10:11][0])
        move4 = Move.fromBytes(bytes[11:12][0])
        originalTrainerId = IntegerField.fromBytes(2, bytes[12:14]).value
        exp = IntegerField.fromBytes(3, bytes[14:17]).value
        hpEv = IntegerField.fromBytes(2, bytes[17:19]).value
        attackEv = IntegerField.fromBytes(2, bytes[19:21]).value
        defenseEv = IntegerField.fromBytes(2, bytes[21:23]).value
        speedEv = IntegerField.fromBytes(2, bytes[23:25]).value
        specialEv = IntegerField.fromBytes(2, bytes[25:27]).value
        iv = IntegerField.fromBytes(2, bytes[27:29]).value
        move1pp = IntegerField.fromBytes(1, bytes[29:30]).value
        move2pp = IntegerField.fromBytes(1, bytes[30:31]).value
        move3pp = IntegerField.fromBytes(1, bytes[31:32]).value
        move4pp = IntegerField.fromBytes(1, bytes[32:33]).value
        level = IntegerField.fromBytes(1, bytes[33:34]).value
        maxHp = IntegerField.fromBytes(2, bytes[34:36]).value
        attack = IntegerField.fromBytes(2, bytes[36:38]).value
        defense = IntegerField.fromBytes(2, bytes[38:40]).value
        speed = IntegerField.fromBytes(2, bytes[40:42]).value
        special = IntegerField.fromBytes(2, bytes[42:44]).value

        return Pokemon(species, currentHp, levelPc, statusAilment, type1, type2, itemHeld, move1, move2, move3, move4, originalTrainerId, exp, hpEv, attackEv, defenseEv, speedEv, specialEv, iv, move1pp, move2pp, move3pp, move4pp, level, maxHp, attack, defense, speed, special, "Missing", "Missing")


# pokemon = Pokemon(
#     Species.CHARIZARD,
#     300,
#     74,
#     StatusAilment.NONE,
#     Type.FIRE,
#     Type.GHOST,
#     Item.CALCIUM,
#     Move.FIRE_BLAST,
#     Move.HYDRO_PUMP,
#     Move.THUNDER_PUNCH,
#     Move.MEGA_KICK,
#     1234,
#     200000,
#     65535,
#     65535,
#     65535,
#     65535,
#     65535,
#     65535,
#     3 << 6,
#     3 << 6,
#     3 << 6,
#     3 << 6,
#     74,
#     300,
#     150,
#     151,
#     152,
#     153,
#     "Alchemy",
#     "BOBBO")
#
# print Pokemon.fromBytes(pokemon.toBytes())