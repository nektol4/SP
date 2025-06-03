class FlagsRegister:
    def __init__(self):
        self.zero = False
        self.negative = False
        self.overflow = False
        self.carry = False

    def update(self, value_bits):
        int_value = int(''.join(str(b) for b in value_bits), 2)
        self.zero = all(b == 0 for b in value_bits)
        self.negative = value_bits[0] == 1
        if int_value >= 2**31:
            self.overflow = True
        else:
            self.overflow = False
        if len(value_bits) > 32:
            self.carry = True
        else:
            self.carry = False
