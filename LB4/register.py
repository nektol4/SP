from flagsregister import FlagsRegister

class Register:
    def __init__(self, name, size=32):
        self.name = name
        self.size = size
        self.value = [0] * self.size
        self.flags = FlagsRegister()

    def load(self, int_value):
        if int_value < -(2**31) or int_value >= 2**31:
            raise ValueError("Value out of range [-2^31, 2^31-1]")
        if int_value < 0:
            int_value = (1 << self.size) + int_value
        bin_str = bin(int_value)[2:].zfill(self.size)
        self.value = [int(b) for b in bin_str]

    def to_int(self):
        if self.value[0] == 0:
            return int(''.join(str(b) for b in self.value), 2)
        else:
            inverted = ''.join(str(1 - b) for b in self.value)
            return -((int(inverted, 2) + 1) & (2**self.size - 1))

    def _update_flags_and_set_value(self, int_result):
        int_result &= (2 ** self.size - 1)
        bin_str = bin(int_result)[2:].zfill(self.size)
        result_bits = [int(b) for b in bin_str]
        self.value = result_bits
        self.flags.update(result_bits)

    def add(self, other):
        int_self = self.to_int()
        int_other = other.to_int()
        int_result = int_self + int_other
        overflow = int_result < -(2**31) or int_result >= 2**31
        if overflow:
            int_result &= (2**self.size - 1)
        self._update_flags_and_set_value(int_result)
        self.flags.overflow = overflow

    def sub(self, other):
        int_self = self.to_int()
        int_other = other.to_int()
        int_result = int_self - int_other
        overflow = int_result < -(2**31) or int_result >= 2**31
        if overflow:
            int_result &= (2**self.size - 1)
        self._update_flags_and_set_value(int_result)
        self.flags.overflow = overflow

    def mul(self, other):
        int_self = self.to_int()
        int_other = other.to_int()
        int_result = int_self * int_other
        overflow = int_result < -(2**31) or int_result >= 2**31
        if overflow:
            int_result &= (2**self.size - 1)
        self._update_flags_and_set_value(int_result)
        self.flags.overflow = overflow

    def div(self, other):
        int_self = self.to_int()
        int_other = other.to_int()
        if int_other == 0:
            raise ZeroDivisionError("Division by zero")
        int_result = int(int_self / int_other)
        self._update_flags_and_set_value(int_result)
        self.flags.overflow = False
