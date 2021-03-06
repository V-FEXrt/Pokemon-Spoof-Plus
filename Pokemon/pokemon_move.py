import random

from pokemon_type import Type


class MoveBase():
    STATUS = 0
    PHYSICAL = 1
    SPECIAL = 2


class Move():
    def __init__(self, name, hex, type, base, power, accuracy, effects):
        self.name = name
        self.hex = hex
        self.type = type
        self.base = base
        self.power = power
        self.accuracy = accuracy
        self.effects = effects

    def __str__(self):
        return self.name

    @staticmethod
    def fromBytes(hex):
        return Move.reverse[hex]

    @staticmethod
    def buildReverse():
        reverse = {}
        Move.members = [attr for attr in dir(Move) if not callable(getattr(Move, attr)) and not attr.startswith("__")]
        for member in Move.members:
            move = getattr(Move, member)
            reverse[move.hex] = move

        Move.reverse = reverse

    @staticmethod
    def rnd():
        return getattr(Move, random.choice(Move.members))


Move.NOTHING = Move("Nothing", 0x00, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.POUND = Move("Pound", 1, Type.NORMAL, MoveBase.PHYSICAL, 40, 100, "--")
Move.KARATE_CHOP = Move("Karate Chop", 2, Type.NORMAL, MoveBase.PHYSICAL, 50, 100, "--")
Move.DOUBLE_SLAP = Move("Double Slap", 3, Type.NORMAL, MoveBase.PHYSICAL, 15, 85, "--")
Move.COMET_PUNCH = Move("Comet Punch", 4, Type.NORMAL, MoveBase.PHYSICAL, 18, 85, "--")
Move.MEGA_PUNCH = Move("Mega Punch", 5, Type.NORMAL, MoveBase.PHYSICAL, 80, 85, "--")
Move.PAY_DAY = Move("Pay Day", 6, Type.NORMAL, MoveBase.PHYSICAL, 40, 100, "--")
Move.FIRE_PUNCH = Move("Fire Punch", 7, Type.FIRE, MoveBase.PHYSICAL, 75, 100, "--")
Move.ICE_PUNCH = Move("Ice Punch", 8, Type.ICE, MoveBase.PHYSICAL, 75, 100, "--")
Move.THUNDER_PUNCH = Move("Thunder Punch", 9, Type.ELECTRIC, MoveBase.PHYSICAL, 75, 100, "--")
Move.SCRATCH = Move("Scratch", 10, Type.NORMAL, MoveBase.PHYSICAL, 40, 100, "--")
Move.VICE_GRIP = Move("Vice Grip", 11, Type.NORMAL, MoveBase.PHYSICAL, 55, 100, "--")
Move.GUILLOTINE = Move("Guillotine", 12, Type.NORMAL, MoveBase.PHYSICAL, 0, 75, "--")
Move.RAZOR_WIND = Move("Razor Wind", 13, Type.NORMAL, MoveBase.SPECIAL, 80, 75, "--")
Move.SWORDS_DANCE = Move("Swords Dance", 14, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.CUT = Move("Cut", 15, Type.NORMAL, MoveBase.PHYSICAL, 50, 95, "--")
Move.GUST = Move("Gust", 16, Type.NORMAL, MoveBase.SPECIAL, 40, 100, "--")
Move.WING_ATTACK = Move("Wing Attack", 17, Type.FLYING, MoveBase.PHYSICAL, 35, 100, "--")
Move.WHIRLWIND = Move("Whirlwind", 18, Type.NORMAL, MoveBase.STATUS, 0, 85, "--")
Move.FLY = Move("Fly", 19, Type.FLYING, MoveBase.PHYSICAL, 90, 95, "--")
Move.BIND = Move("Bind", 20, Type.NORMAL, MoveBase.PHYSICAL, 15, 85, "--")
Move.SLAM = Move("Slam", 21, Type.NORMAL, MoveBase.PHYSICAL, 80, 75, "--")
Move.VINE_WHIP = Move("Vine Whip", 22, Type.GRASS, MoveBase.PHYSICAL, 35, 100, "--")
Move.STOMP = Move("Stomp", 23, Type.NORMAL, MoveBase.PHYSICAL, 65, 100, "--")
Move.DOUBLE_KICK = Move("Double Kick", 24, Type.FIGHTING, MoveBase.PHYSICAL, 30, 100, "--")
Move.MEGA_KICK = Move("Mega Kick", 25, Type.NORMAL, MoveBase.PHYSICAL, 120, 75, "--")
Move.JUMP_KICK = Move("Jump Kick", 26, Type.FIGHTING, MoveBase.PHYSICAL, 100, 95, "--")
Move.ROLLING_KICK = Move("Rolling Kick", 27, Type.FIGHTING, MoveBase.PHYSICAL, 60, 85, "--")
Move.SAND_ATTACK = Move("Sand Attack", 28, Type.NORMAL, MoveBase.STATUS, 0, 100, "--")
Move.HEADBUTT = Move("Headbutt", 29, Type.NORMAL, MoveBase.PHYSICAL, 70, 100, "--")
Move.HORN_ATTACK = Move("Horn Attack", 30, Type.NORMAL, MoveBase.PHYSICAL, 65, 100, "--")
Move.FURY_ATTACK = Move("Fury Attack", 31, Type.NORMAL, MoveBase.PHYSICAL, 15, 85, "--")
Move.HORN_DRILL = Move("Horn Drill", 32, Type.NORMAL, MoveBase.PHYSICAL, 0, 30, "--")
Move.TACKLE = Move("Tackle", 33, Type.NORMAL, MoveBase.PHYSICAL, 40, 100, "--")
Move.BODY_SLAM = Move("Body Slam", 34, Type.NORMAL, MoveBase.PHYSICAL, 85, 100, "--")
Move.WRAP = Move("Wrap", 35, Type.NORMAL, MoveBase.PHYSICAL, 15, 90, "--")
Move.TAKE_DOWN = Move("Take Down", 36, Type.NORMAL, MoveBase.PHYSICAL, 90, 85, "--")
Move.THRASH = Move("Thrash", 37, Type.NORMAL, MoveBase.PHYSICAL, 90, 100, "--")
Move.DOUBLE_EDGE = Move("Double- Edge", 38, Type.NORMAL, MoveBase.PHYSICAL, 100, 100, "--")
Move.TAIL_WHIP = Move("Tail Whip", 39, Type.NORMAL, MoveBase.STATUS, 0, 100, "--")
Move.POISON_STING = Move("Poison Sting", 40, Type.POISON, MoveBase.PHYSICAL, 15, 100, "--")
Move.TWINEEDLE = Move("Twineedle", 41, Type.BUG, MoveBase.PHYSICAL, 25, 100, "--")
Move.PIN_MISSILE = Move("Pin Missile", 42, Type.BUG, MoveBase.PHYSICAL, 14, 85, "--")
Move.LEER = Move("Leer", 43, Type.NORMAL, MoveBase.STATUS, 0, 100, "--")
Move.BITE = Move("Bite", 44, Type.NORMAL, MoveBase.PHYSICAL, 60, 100, "--")
Move.GROWL = Move("Growl", 45, Type.NORMAL, MoveBase.STATUS, 0, 100, "--")
Move.ROAR = Move("Roar", 46, Type.NORMAL, MoveBase.STATUS, 0, 100, "--")
Move.SING = Move("Sing", 47, Type.NORMAL, MoveBase.STATUS, 0, 55, "--")
Move.SUPERSONIC = Move("Supersonic", 48, Type.NORMAL, MoveBase.STATUS, 0, 55, "--")
Move.SONIC_BOOM = Move("Sonic Boom", 49, Type.NORMAL, MoveBase.SPECIAL, 0, 90, "Always deals 20 points of damage")
Move.DISABLE = Move("Disable", 50, Type.NORMAL, MoveBase.STATUS, 0, 55, "--")
Move.ACID = Move("Acid", 51, Type.POISON, MoveBase.SPECIAL, 40, 100, "--")
Move.EMBER = Move("Ember", 52, Type.FIRE, MoveBase.SPECIAL, 40, 100, "--")
Move.FLAMETHROWER = Move("Flamethrower", 53, Type.FIRE, MoveBase.SPECIAL, 90, 100, "--")
Move.MIST = Move("Mist", 54, Type.ICE, MoveBase.STATUS, 0, 0, "--")
Move.WATER_GUN = Move("Water Gun", 55, Type.WATER, MoveBase.SPECIAL, 40, 100, "--")
Move.HYDRO_PUMP = Move("Hydro Pump", 56, Type.WATER, MoveBase.SPECIAL, 120, 80, "--")
Move.SURF = Move("Surf", 57, Type.WATER, MoveBase.SPECIAL, 95, 100, "--")
Move.ICE_BEAM = Move("Ice Beam", 58, Type.ICE, MoveBase.SPECIAL, 95, 100, "--")
Move.BLIZZARD = Move("Blizzard", 59, Type.ICE, MoveBase.SPECIAL, 120, 90, "--")
Move.PSYBEAM = Move("Psybeam", 60, Type.PSYCHIC, MoveBase.SPECIAL, 65, 100, "--")
Move.BUBBLE_BEAM = Move("Bubble Beam", 61, Type.WATER, MoveBase.SPECIAL, 65, 100, "--")
Move.AURORA_BEAM = Move("Aurora Beam", 62, Type.ICE, MoveBase.SPECIAL, 65, 100, "--")
Move.HYPER_BEAM = Move("Hyper Beam", 63, Type.NORMAL, MoveBase.SPECIAL, 150, 90, "--")
Move.PECK = Move("Peck", 64, Type.FLYING, MoveBase.PHYSICAL, 35, 100, "--")
Move.DRILL_PECK = Move("Drill Peck", 65, Type.FLYING, MoveBase.PHYSICAL, 80, 100, "--")
Move.SUBMISSION = Move("Submission", 66, Type.FIGHTING, MoveBase.PHYSICAL, 80, 80, "--")
Move.LOW_KICK = Move("Low Kick", 67, Type.FIGHTING, MoveBase.PHYSICAL, 50, 90, "--")
Move.COUNTER = Move("Counter", 68, Type.FIGHTING, MoveBase.PHYSICAL, 0, 100, "--")
Move.SEISMIC_TOSS = Move("Seismic Toss", 69, Type.FIGHTING, MoveBase.PHYSICAL, 0, 100, "--")
Move.STRENGTH = Move("Strength", 70, Type.NORMAL, MoveBase.PHYSICAL, 80, 100, "--")
Move.ABSORB = Move("Absorb", 71, Type.GRASS, MoveBase.SPECIAL, 20, 100, "--")
Move.MEGA_DRAIN = Move("Mega Drain", 72, Type.GRASS, MoveBase.SPECIAL, 40, 100, "--")
Move.LEECH_SEED = Move("Leech Seed", 73, Type.GRASS, MoveBase.STATUS, 0, 90, "--")
Move.GROWTH = Move("Growth", 74, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.RAZOR_LEAF = Move("Razor Leaf", 75, Type.GRASS, MoveBase.PHYSICAL, 55, 95, "--")
Move.SOLAR_BEAM = Move("Solar Beam", 76, Type.GRASS, MoveBase.SPECIAL, 120, 100, "--")
Move.POISON_POWDER = Move("Poison Powder", 77, Type.POISON, MoveBase.STATUS, 0, 75, "--")
Move.STUN_SPORE = Move("Stun Spore", 78, Type.GRASS, MoveBase.STATUS, 0, 75, "--")
Move.SLEEP_POWDER = Move("Sleep Powder", 79, Type.GRASS, MoveBase.STATUS, 0, 75, "--")
Move.PETAL_DANCE = Move("Petal Dance", 80, Type.GRASS, MoveBase.SPECIAL, 70, 100, "--")
Move.STRING_SHOT = Move("String Shot", 81, Type.BUG, MoveBase.STATUS, 0, 95, "--")
Move.DRAGON_RAGE = Move("Dragon Rage", 82, Type.DRAGON, MoveBase.SPECIAL, 0, 100, "Deals 40 points of damage")
Move.FIRE_SPIN = Move("Fire Spin", 83, Type.FIRE, MoveBase.SPECIAL, 15, 70, "--")
Move.THUNDER_SHOCK = Move("Thunder Shock", 84, Type.ELECTRIC, MoveBase.SPECIAL, 40, 100, "--")
Move.THUNDERBOLT = Move("Thunderbolt", 85, Type.ELECTRIC, MoveBase.SPECIAL, 95, 100, "--")
Move.THUNDER_WAVE = Move("Thunder Wave", 86, Type.ELECTRIC, MoveBase.STATUS, 0, 100, "--")
Move.THUNDER = Move("Thunder", 87, Type.ELECTRIC, MoveBase.SPECIAL, 120, 70, "--")
Move.ROCK_THROW = Move("Rock Throw", 88, Type.ROCK, MoveBase.PHYSICAL, 50, 65, "--")
Move.EARTHQUAKE = Move("Earthquake", 89, Type.GROUND, MoveBase.PHYSICAL, 100, 100, "--")
Move.FISSURE = Move("Fissure", 90, Type.GROUND, MoveBase.PHYSICAL, 0, 30, "Only hits slower targets")
Move.DIG = Move("Dig", 91, Type.GROUND, MoveBase.PHYSICAL, 100, 100, "--")
Move.TOXIC = Move("Toxic", 92, Type.POISON, MoveBase.STATUS, 0, 85, "--")
Move.CONFUSION = Move("Confusion", 93, Type.PSYCHIC, MoveBase.SPECIAL, 50, 100, "--")
Move.PSYCHIC = Move("Psychic", 94, Type.PSYCHIC, MoveBase.SPECIAL, 90, 100, "--")
Move.HYPNOSIS = Move("Hypnosis", 95, Type.PSYCHIC, MoveBase.STATUS, 0, 60, "--")
Move.MEDITATE = Move("Meditate", 96, Type.PSYCHIC, MoveBase.STATUS, 0, 0, "--")
Move.AGILITY = Move("Agility", 97, Type.PSYCHIC, MoveBase.STATUS, 0, 0, "--")
Move.QUICK_ATTACK = Move("Quick Attack", 98, Type.NORMAL, MoveBase.PHYSICAL, 40, 100, "--")
Move.RAGE = Move("Rage", 99, Type.NORMAL, MoveBase.PHYSICAL, 20, 100, "--")
Move.TELEPORT = Move("Teleport", 100, Type.PSYCHIC, MoveBase.STATUS, 0, 0, "--")
Move.NIGHT_SHADE = Move("Night Shade", 101, Type.GHOST, MoveBase.SPECIAL, 0, 100, "--")
Move.MIMIC = Move("Mimic", 102, Type.NORMAL, MoveBase.STATUS, 0, 100, "--")
Move.SCREECH = Move("Screech", 103, Type.NORMAL, MoveBase.STATUS, 0, 85, "--")
Move.DOUBLE_TEAM = Move("Double Team", 104, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.RECOVER = Move("Recover", 105, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.HARDEN = Move("Harden", 106, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.MINIMIZE = Move("Minimize", 107, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.SMOKESCREEN = Move("Smokescreen", 108, Type.NORMAL, MoveBase.STATUS, 0, 100, "--")
Move.CONFUSE_RAY = Move("Confuse Ray", 109, Type.GHOST, MoveBase.STATUS, 0, 100, "--")
Move.WITHDRAW = Move("Withdraw", 110, Type.WATER, MoveBase.STATUS, 0, 0, "--")
Move.DEFENSE_CURL = Move("Defense Curl", 111, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.BARRIER = Move("Barrier", 112, Type.PSYCHIC, MoveBase.STATUS, 0, 0, "--")
Move.LIGHT_SCREEN = Move("Light Screen", 113, Type.PSYCHIC, MoveBase.STATUS, 0, 0, "--")
Move.HAZE = Move("Haze", 114, Type.ICE, MoveBase.STATUS, 0, 0, "--")
Move.REFLECT = Move("Reflect", 115, Type.PSYCHIC, MoveBase.STATUS, 0, 0, "--")
Move.FOCUS_ENERGY = Move("Focus Energy", 116, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.BIDE = Move("Bide", 117, Type.NORMAL, MoveBase.PHYSICAL, 0, 100, "--")
Move.METRONOME = Move("Metronome", 118, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.MIRROR_MOVE = Move("Mirror Move", 119, Type.FLYING, MoveBase.STATUS, 0, 0, "--")
Move.SELF_DESTRUCT = Move("Self-Destruct", 120, Type.NORMAL, MoveBase.PHYSICAL, 260, 100, "--")
Move.EGG_BOMB = Move("Egg Bomb", 121, Type.NORMAL, MoveBase.PHYSICAL, 100, 75, "--")
Move.LICK = Move("Lick", 122, Type.GHOST, MoveBase.PHYSICAL, 20, 100, "--")
Move.SMOG = Move("Smog", 123, Type.POISON, MoveBase.SPECIAL, 20, 70, "--")
Move.SLUDGE = Move("Sludge", 124, Type.POISON, MoveBase.SPECIAL, 65, 100, "--")
Move.BONE_CLUB = Move("Bone Club", 125, Type.GROUND, MoveBase.PHYSICAL, 65, 85, "--")
Move.FIRE_BLAST = Move("Fire Blast", 126, Type.FIRE, MoveBase.SPECIAL, 120, 85, "--")
Move.WATERFALL = Move("Waterfall", 127, Type.WATER, MoveBase.PHYSICAL, 80, 100, "--")
Move.CLAMP = Move("Clamp", 128, Type.WATER, MoveBase.PHYSICAL, 35, 85, "--")
Move.SWIFT = Move("Swift", 129, Type.NORMAL, MoveBase.SPECIAL, 60, 0, "--")
Move.SKULL_BASH = Move("Skull Bash", 130, Type.NORMAL, MoveBase.PHYSICAL, 100, 100, "--")
Move.SPIKE_CANNON = Move("Spike Cannon", 131, Type.NORMAL, MoveBase.PHYSICAL, 20, 100, "--")
Move.CONSTRICT = Move("Constrict", 132, Type.NORMAL, MoveBase.PHYSICAL, 10, 100, "--")
Move.AMNESIA = Move("Amnesia", 133, Type.PSYCHIC, MoveBase.STATUS, 0, 0, "--")
Move.KINESIS = Move("Kinesis", 134, Type.PSYCHIC, MoveBase.STATUS, 0, 80, "--")
Move.SOFT_BOILED = Move("Soft-Boiled", 135, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.HIGH_JUMP_KICK = Move("High Jump Kick", 136, Type.FIGHTING, MoveBase.PHYSICAL, 85, 90, "--")
Move.GLARE = Move("Glare", 137, Type.NORMAL, MoveBase.STATUS, 0, 75, "--")
Move.DREAM_EATER = Move("Dream Eater", 138, Type.PSYCHIC, MoveBase.SPECIAL, 100, 100, "--")
Move.POISON_GAS = Move("Poison Gas", 139, Type.POISON, MoveBase.STATUS, 0, 55, "--")
Move.BARRAGE = Move("Barrage", 140, Type.NORMAL, MoveBase.PHYSICAL, 15, 85, "--")
Move.LEECH_LIFE = Move("Leech Life", 141, Type.BUG, MoveBase.PHYSICAL, 20, 100, "--")
Move.LOVELY_KISS = Move("Lovely Kiss", 142, Type.NORMAL, MoveBase.STATUS, 0, 75, "--")
Move.SKY_ATTACK = Move("Sky Attack", 143, Type.FLYING, MoveBase.PHYSICAL, 140, 90, "--")
Move.TRANSFORM = Move("Transform", 144, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.BUBBLE = Move("Bubble", 145, Type.WATER, MoveBase.SPECIAL, 20, 100, "--")
Move.DIZZY_PUNCH = Move("Dizzy Punch", 146, Type.NORMAL, MoveBase.PHYSICAL, 70, 100, "--")
Move.SPORE = Move("Spore", 147, Type.GRASS, MoveBase.STATUS, 0, 100, "--")
Move.FLASH = Move("Flash", 148, Type.NORMAL, MoveBase.STATUS, 0, 70, "--")
Move.PSYWAVE = Move("Psywave", 149, Type.PSYCHIC, MoveBase.SPECIAL, 0, 80, "--")
Move.SPLASH = Move("Splash", 150, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.ACID_ARMOR = Move("Acid Armor", 151, Type.POISON, MoveBase.STATUS, 0, 0, "--")
Move.CRABHAMMER = Move("Crabhammer", 152, Type.WATER, MoveBase.PHYSICAL, 90, 85, "--")
Move.EXPLOSION = Move("Explosion", 153, Type.NORMAL, MoveBase.PHYSICAL, 340, 100, "--")
Move.FURY_SWIPES = Move("Fury Swipes", 154, Type.NORMAL, MoveBase.PHYSICAL, 18, 80, "--")
Move.BONEMERANG = Move("Bonemerang", 155, Type.GROUND, MoveBase.PHYSICAL, 50, 90, "--")
Move.REST = Move("Rest", 156, Type.PSYCHIC, MoveBase.STATUS, 0, 0, "--")
Move.ROCK_SLIDE = Move("Rock Slide", 157, Type.ROCK, MoveBase.PHYSICAL, 75, 90, "--")
Move.HYPER_FANG = Move("Hyper Fang", 158, Type.NORMAL, MoveBase.PHYSICAL, 80, 90, "--")
Move.SHARPEN = Move("Sharpen", 159, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.CONVERSION = Move("Conversion", 160, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.TRI_ATTACK = Move("Tri Attack", 161, Type.NORMAL, MoveBase.SPECIAL, 80, 100, "--")
Move.SUPER_FANG = Move("Super Fang", 162, Type.NORMAL, MoveBase.PHYSICAL, 0, 90, "--")
Move.SLASH = Move("Slash", 163, Type.NORMAL, MoveBase.PHYSICAL, 70, 100, "--")
Move.SUBSTITUTE = Move("Substitute", 164, Type.NORMAL, MoveBase.STATUS, 0, 0, "--")
Move.STRUGGLE = Move("Struggle", 165, Type.NORMAL, MoveBase.PHYSICAL, 50, 100, "--")

Move.buildReverse()
