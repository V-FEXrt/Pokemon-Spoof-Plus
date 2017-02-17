class Type():
    def __init__(self, name, hex):
        self.name = name
        self.hex = hex

    def __str__(self):
        return  self.name

    @staticmethod
    def fromHex(hex):
        return Type.reverse[hex]

    @staticmethod
    def buildReverse():
        reverse = {}
        for member in [attr for attr in dir(Type) if not callable(getattr(Type, attr)) and not attr.startswith("__")]:
            type = getattr(Type, member)
            reverse[type.hex] = type

        Type.reverse = reverse

Type.NORMAL = Type("Normal", 0x00)
Type.FIGHTING = Type("Fighting", 0x01)
Type.FLYING = Type("Flying", 0x02)
Type.POISON = Type("Poison", 0x03)
Type.GROUND = Type("Ground", 0x04)
Type.ROCK = Type("Rock", 0x05)
Type.BUG = Type("Bug", 0x07)
Type.GHOST = Type("Ghost", 0x08)
Type.FIRE = Type("Fire", 0x14)
Type.WATER = Type("Water", 0x15)
Type.GRASS = Type("Grass", 0x16)
Type.ELECTRIC = Type("Electric", 0x17)
Type.PSYCHIC = Type("Psychic", 0x18)
Type.ICE = Type("Ice", 0x19)
Type.DRAGON = Type("Dragon", 0x1A)

Type.buildReverse()
