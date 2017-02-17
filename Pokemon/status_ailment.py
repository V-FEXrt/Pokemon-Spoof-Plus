class StatusAilment():
    def __init__(self, name, hex):
        self.name = name
        self.hex = hex

    def __str__(self):
        return  self.name

    @staticmethod
    def fromHex(hex):
        return StatusAilment.reverse[hex]

    @staticmethod
    def buildReverse():
        reverse = {}
        for member in [attr for attr in dir(StatusAilment) if not callable(getattr(StatusAilment, attr)) and not attr.startswith("__")]:
            statusAilment = getattr(StatusAilment, member)
            reverse[statusAilment.hex] = statusAilment

        StatusAilment.reverse = reverse

StatusAilment.NONE = StatusAilment("None", 0x00)
StatusAilment.ASLEEP = StatusAilment("Asleep", 0x04)
StatusAilment.POISONED = StatusAilment("Poisoned", 0x08)
StatusAilment.BURNED = StatusAilment("Burned", 0x10)
StatusAilment.FROZEN = StatusAilment("Frozen", 0x20)
StatusAilment.PARALYZED = StatusAilment("Paralyzed", 0x40)

StatusAilment.buildReverse()
