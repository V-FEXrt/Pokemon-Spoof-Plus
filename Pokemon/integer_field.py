class IntegerField():
    def __init__(self, value, bytes):
            self.value = value
            self.bytes = bytes

    def toHex(self):
        low = hex(self.value & 0xFF)
        mid = hex((self.value >> 8) & 0xFF)
        high = hex((self.value >> 16) & 0xFF)

        if(self.bytes == 3):
            return [high, mid, low]
        if(self.bytes == 2):
            return [mid, low]
        return [low]
