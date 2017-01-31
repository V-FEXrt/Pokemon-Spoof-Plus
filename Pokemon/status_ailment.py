class StatusAilment():
    def __init__(self, name, hex):
        self.name = name
        self.hex = hex

StatusAilment.NONE = StatusAilment("None", 0x00)
StatusAilment.ASLEEP = StatusAilment("Asleep", 0x04)
StatusAilment.POISONED = StatusAilment("Poisoned", 0x08)
StatusAilment.BURNED = StatusAilment("Burned", 0x10)
StatusAilment.FROZEN = StatusAilment("Frozen", 0x20)
StatusAilment.PARALYZED = StatusAilment("Paralyzed", 0x40)
