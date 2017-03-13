class IntegerField():
    def __init__(self, value, byte_count):
        self.value = int(value)
        self.bytes = int(byte_count)

    def __str__(self):
        return str(self.value)

    def toBytes(self):
        low = self.value & 0xFF
        mid = (self.value >> 8) & 0xFF
        high = (self.value >> 16) & 0xFF

        if(self.bytes == 3):
            return [high, mid, low]
        if(self.bytes == 2):
            return [mid, low]
        return [low]

    @staticmethod
    def fromBytes(byte_count, bytes):
        val = 0
        if(byte_count == 3):
            val = int((bytes[0] << 16) | (bytes[1] << 8)  | (bytes[2]))
        elif(byte_count == 2):
            val = int((bytes[0] << 8)  | (bytes[1]))
        else:
            val = int(bytes[0])
        return IntegerField(val, byte_count)


#i = IntegerField(0xdedbef, 3)
#print i
#print IntegerField.fromHex(3, i.toBytes())