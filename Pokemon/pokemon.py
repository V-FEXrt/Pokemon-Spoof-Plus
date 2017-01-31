from integer_field import IntegerField
from Utilities.text_converter import *

class Pokemon():
    def __init__(self, species, currentHp, levelPc, statusAilment, type1, type2, itemHeld, move1, move2, move3, move4,
                 originalTrainerId, exp, hpEv, attackEv, defenseEv, speedEv, specialEv, iv, move1pp, move2pp, move3pp,
                 move4pp, level, maxHp, attack, defense, speed, special, nickname, originalTrainerName):
        self.species = species
        self.currentHp = IntegerField(currentHp, 2)
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

        self.nickname = nickname
        if(len(nickname) > 10):
            raise ValueError("Nickname cannot be longer that 10 characters")

        self.originalTrainerName = originalTrainerName
        if(len(originalTrainerName) > 7):
            raise ValueError("Trainer name cannot be longer than 7 characters")

    def terminatedNickname(self):
        return padTo(terminate(convert(self.nickname)), "0x50", 11)

    def extend(self, bytes, arr):
        for a in arr:
            bytes.append(a)

    def toBytes(self):
        bytes = []

        bytes.append(hex(self.species.hex))
        self.extend(bytes, self.currentHp.toHex())

        self.extend(bytes, self.levelPc.toHex())
        bytes.append(hex(self.statusAilment.hex))
        bytes.append(hex(self.type1.hex))
        bytes.append(hex(self.type2.hex))
        bytes.append(hex(self.itemHeld.hex))
        bytes.append(hex(self.move1.hex))
        bytes.append(hex(self.move2.hex))
        bytes.append(hex(self.move3.hex))
        bytes.append(hex(self.move4.hex))
        self.extend(bytes, self.originalTrainerId.toHex())
        self.extend(bytes, self.exp.toHex())
        self.extend(bytes, self.hpEv.toHex())
        self.extend(bytes, self.attackEv.toHex())
        self.extend(bytes, self.defenseEv.toHex())
        self.extend(bytes, self.speedEv.toHex())
        self.extend(bytes, self.specialEv.toHex())
        self.extend(bytes, self.iv.toHex())
        self.extend(bytes, self.move1pp.toHex())
        self.extend(bytes, self.move2pp.toHex())
        self.extend(bytes, self.move3pp.toHex())
        self.extend(bytes, self.move4pp.toHex())
        self.extend(bytes, self.level.toHex())
        self.extend(bytes, self.maxHp.toHex())
        self.extend(bytes, self.attack.toHex())
        self.extend(bytes, self.defense.toHex())
        self.extend(bytes, self.speed.toHex())
        self.extend(bytes, self.special.toHex())

        return bytes
