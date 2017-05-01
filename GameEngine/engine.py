from Pokemon.pokemon_move import MoveBase
from Pokemon.pokemon_type import Type

import random

def process(ai_pokemon, ai_move, enemy_pokemon, enemy_move):
    ai_dealt_damage = calculate_damage(ai_pokemon, enemy_pokemon, ai_move)
    enemy_dealt_damage = calculate_damage(enemy_pokemon, ai_pokemon, enemy_move)

    if(ai_pokemon.speed.value > enemy_pokemon.speed.value):
        print ai_pokemon.species.name + " is faster"
        enemy_pokemon.currentHp.value -= ai_dealt_damage
        ai_pokemon.currentHp.value -= enemy_dealt_damage
    else:
        print enemy_pokemon.species.name + " is faster"
        ai_pokemon.currentHp.value -= enemy_dealt_damage
        enemy_pokemon.currentHp.value -= ai_dealt_damage

    print enemy_pokemon.species.name + " dealt " + str(enemy_dealt_damage) + " to " + ai_pokemon.species.name
    print ai_pokemon.species.name + " dealt " + str(ai_dealt_damage) + " to " + enemy_pokemon.species.name

def calculate_damage(attacker, defender, move):
    # ((2A/5+2)*B*C)/D)/50)+2)*X)*Y/10)*Z)/255
    #
    # A = attacker's Level
    # B = attacker's Attack or Special
    # C = attack Power
    # D = defender's Defense or Special
    # X = same-Type attack bonus (1 or 1.5)
    # Y = Type modifiers (40, 20, 10, 5, 2.5, or 0)
    # Z = a random number between 217 and 255

    A = attacker.level.value

    B = attacker.attack.value
    D = defender.defense.value
    if(move.type == MoveBase.SPECIAL):
        B = attacker.special.value
        D = defender.special.value

    C = move.power
    X = 1

    if(attacker.type1 == move.type or attacker.type2 == move.type):
        X = 1.5


    Y = type_modifiers(move, defender)

    Z = random.randrange(217, 256)

    return ((((((((2*A/5+2)*B*C)/D)/50)+2)*X)*Y/10)*Z)/255

def type_modifiers(move, defender):
    # call twice if type1 != type 2
    # Y = Type modifiers (40, 20, 10, 5, 2.5, or 0)
    y1 = type_chart[move.type.hex][defender.type1.hex]
    y2 = type_chart[move.type.hex][defender.type2.hex]

    if defender.type1.hex == defender.type2.hex:
        return y1 * 10

    return y1 * y2 * 10


# build type chart.

# Defaults everything to 1x effective
type_chart = {}

for hex1 in Type.hex_keys:
    type_chart[hex1] = {}
    for hex2 in Type.hex_keys:
        type_chart[hex1][hex2] = 1

normal = type_chart[Type.NORMAL.hex]
normal[Type.ROCK.hex] = 0.5
normal[Type.GHOST.hex] = 0

fighting = type_chart[Type.FIGHTING.hex]
fighting[Type.NORMAL.hex] = 2
fighting[Type.FLYING.hex] = 0.5
fighting[Type.POISON.hex] = 0.5
fighting[Type.ROCK.hex] = 2
fighting[Type.BUG.hex] = 0.5
fighting[Type.GHOST.hex] = 0
fighting[Type.PSYCHIC.hex] = 0.5
fighting[Type.ICE.hex] = 2

flying = type_chart[Type.FLYING.hex]
flying[Type.FIGHTING.hex] = 2
flying[Type.ROCK.hex] = 0.5
flying[Type.BUG.hex] = 2
flying[Type.GRASS.hex] = 2
flying[Type.ELECTRIC.hex] = 0.5

poison = type_chart[Type.POISON.hex]
poison[Type.POISON.hex] = 0.5
poison[Type.GROUND.hex] = 0.5
poison[Type.ROCK.hex] = 0.5
poison[Type.BUG.hex] = 2
poison[Type.GHOST.hex] = 0.5
poison[Type.GRASS.hex] = 2

ground = type_chart[Type.GROUND.hex]
ground[Type.FLYING.hex] = 0
ground[Type.POISON.hex] = 2
ground[Type.ROCK.hex] = 2
ground[Type.BUG.hex] = 0.5
ground[Type.FIRE.hex] = 2
ground[Type.GRASS.hex] = 0.5
ground[Type.ELECTRIC.hex] = 2

rock = type_chart[Type.ROCK.hex]
rock[Type.FIGHTING.hex] = 0.5
rock[Type.FLYING.hex] = 2
rock[Type.GROUND.hex] = 0.5
rock[Type.BUG.hex] = 2
rock[Type.FIRE.hex] = 2
rock[Type.ICE.hex] = 2


bug = type_chart[Type.BUG.hex]
bug[Type.FIGHTING.hex] = 0.5
bug[Type.FLYING.hex] = 0.5
bug[Type.POISON.hex] = 2
bug[Type.GHOST.hex] = 0.5
bug[Type.FIRE.hex] = 0.5
bug[Type.GRASS.hex] = 2
bug[Type.PSYCHIC.hex] = 2

ghost = type_chart[Type.GHOST.hex]
ghost[Type.NORMAL.hex] = 0
ghost[Type.GHOST.hex] = 2
ghost[Type.PSYCHIC.hex] = 0

fire = type_chart[Type.FIRE.hex]
fire[Type.ROCK.hex] = 0.5
fire[Type.BUG.hex] = 2
fire[Type.FIRE.hex] = 0.5
fire[Type.WATER.hex] = 0.5
fire[Type.GRASS.hex] = 2
fire[Type.ICE.hex] = 2
fire[Type.DRAGON.hex] = 0.5

water = type_chart[Type.WATER.hex]
water[Type.GROUND.hex] = 2
water[Type.ROCK.hex] = 2
water[Type.FIRE.hex] = 2
water[Type.WATER.hex] = 0.5
water[Type.GRASS.hex] = 0.5
water[Type.DRAGON.hex] = 0.5

grass = type_chart[Type.GRASS.hex]
grass[Type.FLYING.hex] = 0.5
grass[Type.POISON.hex] = 0.5
grass[Type.GROUND.hex] = 2
grass[Type.ROCK.hex] = 2
grass[Type.BUG.hex] = 0.5
grass[Type.FIRE.hex] = 0.5
grass[Type.WATER.hex] = 2
grass[Type.GRASS.hex] = 0.5
grass[Type.DRAGON.hex] = 0.5

electric = type_chart[Type.ELECTRIC.hex]
electric[Type.FLYING.hex] = 2
electric[Type.GROUND.hex] = 0
electric[Type.WATER.hex] = 2
electric[Type.GRASS.hex] = 0.5
electric[Type.ELECTRIC.hex] = 0.5
electric[Type.DRAGON.hex] = 0.5

psychic = type_chart[Type.PSYCHIC.hex]
psychic[Type.FIGHTING.hex] = 2
psychic[Type.POISON.hex] = 2
psychic[Type.PSYCHIC.hex] = 0.5

ice = type_chart[Type.ICE.hex]
ice[Type.FLYING.hex] = 2
ice[Type.GROUND.hex] = 2
ice[Type.WATER.hex] = 0.5
ice[Type.GRASS.hex] = 2
ice[Type.ICE.hex] = 0.5
ice[Type.DRAGON.hex] = 2

dragon = type_chart[Type.DRAGON.hex]
dragon[Type.DRAGON.hex] = 2