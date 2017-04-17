import random

from pokemon_type import Type

class MoveBase():
    NDA  = 0
    PHYS = 1
    SPEC = 2
    CALC = 3

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

Move.NOTHING = Move("Nothing", 0x00, Type.NORMAL, MoveBase.NDA, 0, 0, "")
Move.POUND = Move("Pound", 0x01)
Move.KARATE_CHOP = Move("Karate Chop", 0x02, Type.NORMAL, MoveBase.PHYS, 50, 99.6, "--")
Move.DOUBLE_SLAP = Move("Double Slap", 0x03)
Move.COMET_PUNCH = Move("Comet Punch", 0x04)
Move.MEGA_PUNCH = Move("Mega Punch", 0x05, Type.NORMAL, 80, 84.4, "--")
Move.PAY_DAY = Move("Pay Day", 0x06)
Move.FIRE_PUNCH = Move("Fire Punch", 0x07, Type.FIRE, MoveBase.SPEC, 75, 99.6, "Burn (10% chance)")
Move.ICE_PUNCH = Move("Ice Punch", 0x08, Type.ICE, MoveBase.SPEC, 75, 99.6, "Freeze (10% chance)")
Move.THUNDER_PUNCH = Move("Thunder Punch ", 0x09, Type.ELECTRIC, MoveBase.SPEC, 75, 99.6, "Paralyze (10% chance)")
Move.GUST = Move("Gust", 0x10)
Move.WING_ATTACK = Move("Wing Attack", 0x11, Type.FLYING, MoveBase.PHYS, 35, 99.6, "--")
Move.WHIRLWIND = Move("Whirlwind", 0x12)
Move.FLY = Move("Fly", 0x13, Type.FLYING, 70, 94.5, "Invulnerable for a turn, then attack")
Move.BIND = Move("Bind", 0x14)
Move.SLAM = Move("Slam", 0x15, Type.NORMAL, MoveBase.PHYS, 80, 74.6, "--")
Move.VINE_WHIP = Move("Vine Whip", 0x16, Type.GRASS, MoveBase.SPEC, 35, 99.6, "--")
Move.STOMP = Move("Stomp", 0x17, Type.NORMAL, MoveBase.PHYS, 65, 99.6, "Flinch (30% chance)")
Move.DOUBLE_KICK = Move("Double Kick", 0x18, Type.FIGHTING, MoveBase.PHYS, 30, 99.6, "Hits twice")
Move.MEGA_KICK = Move("Mega Kick", 0x19, Type.NORMAL, MoveBase.PHYS, 120, 74.6, "--")
Move.JUMP_KICK = Move("Jump Kick", 0x1A, Type.FIGHTING, MoveBase.PHYS, 70, 94.5, "12.5% recoil damage if miss")
Move.ROLLING_KICK = Move("Rolling Kick", 0x1B, Type.FIGHTING, MoveBase.PHYS, 60, 84.4, "Flinch (30% chance)")
Move.SAND_ATTACK = Move("Sand Attack", 0x1C)
Move.HEADBUTT = Move("Headbutt", 0x1D, Type.NORMAL, MoveBase.PHYS, 70, 99.6, "Flinch (30% chance)")
Move.HORN_ATTACK = Move("Horn Attack", 0x1E, Type.NORMAL, MoveBase.PHYS, 65, 99.6, "--")
Move.FURY_ATTACK = Move("Fury Attack", 0x1F)
Move.HORN_DRILL = Move("Horn Drill", 0x20)
Move.TACKLE = Move("Tackle", 0x21)
Move.BODY_SLAM = Move("Body Slam", 0x22, Type.NORMAL, MoveBase.PHYS, 85, 99.6, "Paralyze (30% chance)")
Move.WRAP = Move("Wrap", 0x23)
Move.TAKE_DOWN = Move("Take Down ", 0x24, Type.NORMAL, MoveBase.PHYS, 90, 84.4, "Attacker goes nuts")
Move.TRASH = Move("Trash", 0x25)
Move.DOUBLE_EDGE = Move("Double Edge", 0x26, Type.NORMAL, MoveBase.PHYS, 100, 99.6, "25% recoil damage")
Move.TAIL_WHIP = Move("Tail Whip", 0x27)
Move.POISON_STING = Move("Poison Sting", 0x28)
Move.TWIN_NEEDLE = Move("Twin Needle", 0x29, Type.BUG, MoveBase.PHYS, 25, 99.6, "Hits twice/ poison (20% chance)")
Move.PIN_MISSLE = Move("Pin Missle", 0x2A, Type.BUG, MoveBase.PHYS, 14, 84.4, "Hits 2 to 5 times")
Move.LEER = Move("Leer", 0x2B)
Move.BITE = Move("Bite", 0x2C, Type.NORMAL, MoveBase.PHYS, 60, 99.6, "Flinch (10% chance)")
Move.GROWL = Move("Growl", 0x2D)
Move.ROAR = Move("Roar", 0x2E)
Move.SUPER_SONIC = Move("SuperSonic", 0x2F)
Move.SONIC_BOOM = Move("Sonic Boom", 0x30)
Move.DISABLE = Move("Disable", 0x32)
Move.ACID = Move("Acid", 0x33)
Move.EMBER = Move("Ember", 0x34, Type.FIRE, MoveBase.SPEC, 40, 99.6, "Burn (10% chance)")
Move.FLAMETHROWER = Move("Flamethrower", 0x35, Type.FIRE, MoveBase.SPEC, 95, 99.6, "Burn (10% chance)")
Move.MIST = Move("Mist", 0x36)
Move.WATER_GUN = Move("Water Gun", 0x37)
Move.HYDRO_PUMP = Move("Hydro Pump", 0x38)
Move.SURF = Move("Surf", 0x39)
Move.ICE_BEAM = Move("Ice Beam", 0x3A, Type.ICE, MoveBase.SPEC, 95, 99.6, "Freeze (10% chance)")
Move.BLIZZARD = Move("Blizzard", 0x3B, Type.ICE, MoveBase.SPEC, 120, 89.5, "Freeze (10% chance)")
Move.PSY_BEAM = Move("PsyBeam", 0x3C)
Move.BUBBLE_BEAM = Move("Bubble Beam", 0x3D)
Move.AURORA_BEAM = Move("Aurora Beam", 0x3E, Type.ICE, MoveBase.SPEC, 65, 99.6, "Lower victim attack (10% chance)")
Move.HYPER_BEAM = Move("Hyper Beam", 0x3F, Type.NORMAL, MoveBase.PHYS, 150, 89.5, "Attack, then lose a turn")
Move.PECK = Move("Peck", 0x40, Type.FLYING, MoveBase.PHYS, 35, 99.6, "--")
Move.DRILL_PECK = Move("Drill Peck", 0x41, Type.FLYING, MoveBase.PHYS, 80, 99.6, "--")
Move.SUBMISSION = Move("Submission", 0x42, Type.FIGHTING, MoveBase.PHYS, 80, 79.7, "25% recoil damage")
Move.LOW_KICK = Move("Low Kick", 0x43, Type.FIGHTING, MoveBase.PHYS, 50, 89.5, "Flinch (30% chance)")
Move.COUNTER = Move("Counter", 0x44, Type.FIGHTING, MoveBase.CALC, 0, 99.6, "Inflict twice damage taken")
Move.SEISMIC_TOSS = Move("Seismic Toss", 0x45, Type.FIGHTING, MoveBase.CALC, 0, 99.6, "Inflict 1 HP per level of attacker")
Move.STRENGTH = Move("Strength", 0x46, Type.NORMAL, MoveBase.PHYS, 80, 99.6, "--")
Move.ABSORB = Move("Absorb", 0x47, Type.GRASS, MoveBase.SPEC, 20, 99.6, "Attacker recovers 50% of damage")
Move.MEGA_DRAIN = Move("Mega Drain", 0x48, Type.GRASS, MoveBase.SPEC, 40, 99.6, "Attacker recovers 50% of damage")
Move.LEECH_SEED = Move("Leech Seed", 0x49, Type.GRASS, MoveBase.CALC, 0, 89.5, "Continually suck HP")
Move.GROWTH = Move("Growth", 0x4A)
Move.RAZOR_WIND = Move("Razor Wind", 0x4B, Type.NORMAL, MoveBase.PHYS, 80, 74.6, "Lose a turn, then attack")
Move.SOLAR_BEAM = Move("Solar Beam", 0x4C, Type.GRASS, MoveBase.SPEC, 120, 99.6, "Lose a turn, then attack")
Move.POISON_POWDER = Move("Poison Powder", 0x4D)
Move.STUN_SPORE = Move("Stun Spore", 0x4E, Type.GRASs, MoveBase.NDA, 0, 74.6, "Paralysis (100% chance)")
Move.SLEEP_POWDER = Move("Sleep Powder", 0x4F, Type.GRASS, MoveBase.NDA, 0, 74.6, "Sleep (100% chance)")
Move.PETAL_DANCE = Move("Petal Dance", 0x50, Type.GRASS, MoveBase.SPEC, 70, 99.6, "Attacker goes nuts")
Move.STRING_SHOT = Move("String Shot", 0x51, Type.BUG, MoveBase.NDA, 0, 94.5, "Lower victim Speed")
Move.DRAGON_RAGE = Move("Dragon Rage", 0x52, Type.DRAGON, MoveBase.CALC, 0, 99.6, "Inflict exactly 40 HP")
Move.FIRE_SPIN = Move("Fire Spin", 0x53, Type.FIRE, MoveBase.SPEC, 15, 69.5, "Multi-turn Attack/Immobilize victim")
Move.THUNDER_SHOCK = Move("ThunderShock", 0x54, Type.ELECTRIC, MoveBase.SPEC, 40, 99.6, "Paralyze (10% chance)")
Move.THUNDER_BOLT = Move("ThunderBolt", 0x55, Type.ELECTRIC, MoveBase.SPEC, 95, 99.6, "Paralyze (10% chance)")
Move.THUNDER_WAVE = Move("ThunderWave", 0x56, Type.ELECTRIC, MoveBase.NDA, 0, 99.6, "Paralyze (100% chance)")
Move.THUNDER = Move("Thunder", 0x57, Type.ELECTRIC, MoveBase.SPEC, 120, 69.5, "Paralyze (10% chance)")
Move.ROCK_THROW = Move("Rock Throw", 0x58)
Move.EARTH_QUAKE = Move("EarthQuake", 0x59, Type.GROUND, MoveBase.PHYS, 100, 99.6, "--")
Move.FISSURE = Move("Fissure", 0x5A, Type.GROUND, MoveBase.CALC, 0, 29.7, "one-hit KO")
Move.DIG = Move("Dig", 0x5B, Type.GROUND, MoveBase.PHYS, 100, 99.6, "Invulnerable for a turn, then attack")
Move.TOXIC = Move("Toxic", 0x5C)
Move.CONFUSION = Move("Confusion", 0x5D)
Move.PSYCHIC = Move("Psychic", 0x5E)
Move.HYPNOSIS = Move("Hypnosis", 0x5F)
Move.MEDITATE = Move("Meditate", 0x60)
Move.AGILITY = Move("Agility", 0x61)
Move.QUICK_ATTACK = Move("Quick Attack", 0x62)
Move.RAGE = Move("Rage", 0x63)
Move.TELEPORT = Move("Teleport", 0x64)
Move.NIGHT_SHADE = Move("Night Shade", 0x65, Type.GHOST, MoveBase.CALC, 0, 99.6, "Inflict 1 HP per level of attacker")
Move.MIMIC = Move("Mimic", 0x66)
Move.SCREECH = Move("Screech", 0x67)
Move.DOUBLE_TEAM = Move("Double Team", 0x68)
Move.RECOVER = Move("Recover", 0x69)
Move.HARDEN = Move("Harden", 0x6A)
Move.MINIMIZED = Move("Minimized", 0x6B)
Move.SMOKE_SCREEN = Move("Smoke Screen", 0x6C)
Move.CONFUSE_RAY = Move("Confuse Ray", 0x6D, Type.GHOST, MoveBase.NDA, 0, 99.6, "Confuse (100% chance)")
Move.WITH_DRAW = Move("WithDraw", 0x6E)
Move.DEFENCE_CURL = Move("Defence Curl", 0x6F)
Move.BARRIER = Move("Barrier", 0x70)
Move.LIGHTSCREEN = Move("Light screen", 0x71)
Move.HAZE = Move("Haze", 0x72)
Move.REFLECT = Move("Reflect", 0x73)
Move.FOCUS = Move("Focus", 0x74)
Move.BIDE = Move("Bide", 0x75)
Move.METRONOME = Move("Metronome", 0x76)
Move.MIRROR_MOVE = Move("Mirror Move", 0x77, Type.FLYING, MoveBase.CALC, 0, 99.6, "Copy opponents last attack")
Move.SELF_DESTRUCT = Move("Self Destruct", 0x78, Type.NORMAL, MoveBase.PHYS, 260, 99.6, "Attacker faints")
Move.EGG_BOMB = Move("Egg Bomb", 0x79, Type.NORMAL, MoveBase.PHYS, 100, 74.6, "--")
Move.LICK = Move("Lick", 0x7A, Type.GHOST, MoveBase.PHYS, 20, 99.6, "Paralyze (30% chance)")
Move.SMOG = Move("Smog", 0x7B)
Move.SLUDGE = Move("Sludge", 0x7C)
Move.BONE_CLUB = Move("Bone Club", 0x7D, Type.GROUND, MoveBase.PHYS, 65, 84.4, "Flinch (10% chance)")
Move.FIRE_BLAST = Move("Fire Blast", 0x7E, Type.FIRE, MoveBase.SPEC, 120, 84.4, "Burn (30% chance)")
Move.WATERFALL = Move("Waterfall", 0x7F)
Move.CLAMP = Move("Clamp", 0x80)
Move.SWIFT = Move("Swift", 0x81, Type.NORMAL, MoveBase.PHYS, 60, 99.6, "Hit rate is always 99.6")
Move.SKULL_BASH = Move("Skull Bash", 0x82, Type.NORMAL, MoveBase.PHYS, 100, 99.6, "Lose a turn, then attack")
Move.SPIKE_CANNON = Move("Spike Cannon", 0x83)
Move.CONSTRICT = Move("Constrict", 0x84)
Move.AMNESIA = Move("Amnesia", 0x85)
Move.KINESIS = Move("Kinesis", 0x86)
Move.SOFTBOILED = Move("Softboiled", 0x87)
Move.HI_JUMP_KICK = Move("Hi-Jump Kick", 0x88, Type.FIGHTING, MoveBase.PHYS, 85, 89.5, "1 HP recoil damage if miss")
Move.GLARE = Move("Glare", 0x89)
Move.DREAM_EATER = Move("Dream Eater", 0x8A)
Move.POISON_GAS = Move("Poison Gas", 0x8B)
Move.BARRAGE = Move("Barrage", 0x8C)
Move.LEECH_LIFE = Move("Leech Life", 0x8D, Type.BUG, MoveBase.PHYS, 20, 99.6, "Attacker recovers 50% damage")
Move.LOVELY_KISS = Move("Lovely Kiss", 0x8E)
Move.SKY_ATTACK = Move("Sky Attack", 0x8F, Type.FLYING, MoveBase.PHYS, 140, 89.5, "Lose a turn, then attack")
Move.TRANSFORM = Move("Transform", 0x90)
Move.BUBBLE = Move("Bubble", 0x91)
Move.DIZZY_PUNCH = Move("Dizzy Punch", 0x92, Type.NORMAL, MoveBase.PHYS, 70, 99.6, "--")
Move.SPORE = Move("Spore", 0x93, Type.GRASS, MoveBase.NDA, 0, 99.6, "Sleep (100% chance)")
Move.FLASH = Move("Flash", 0x94)
Move.PSYWAVE = Move("Psywave", 0x95)
Move.SPLASH = Move("Splash", 0x96)
Move.ACID_ARMOR = Move("Acid Armor", 0x97)
Move.CRABHAMMER = Move("Crabhammer", 0x98)
Move.EXPLOSION = Move("Explosion", 0x99, Type.NORMAL, MoveBase.PHYS, 340, 99.6, "Attacker faints")
Move.FURY_SWIPE = Move("Fury Swipe", 0x9A)
Move.BONEMERANG = Move("Bonemerang", 0x9B, Type.GROUND, MoveBase.PHYS, 50, 89.5, "Hits twice")
Move.REST = Move("Rest", 0x9C)
Move.ROCK_SLIDE = Move("Rock Slide", 0x9D)
Move.HYPER_FANG = Move("Hyper Fang", 0x9E, Type.NORMAL, MoveBase.PHYS, 80, 89.5, "Flinch (10% chance)")
Move.SHARPEN = Move("Sharpen", 0x9F)
Move.CONVERSION = Move("Conversion", 0xA0)
Move.TRI_ATTACK = Move("Tri Attack", 0xA1, Type.NORMAL, MoveBase.PHYS, 80, 99.6, "--")
Move.SUPER_FANG = Move("Super Fang", 0xA2)
Move.SLASH = Move("Slash", 0xA3, Type.NORMAL, MoveBase.PHYS, 70, 99.6, "High crit chance")
Move.SUBSTITUTE = Move("Substitute", 0xA4)
Move.STRUGGLE = Move("Struggle", 0xA5)

Move.buildReverse()
