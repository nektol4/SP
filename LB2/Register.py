from FlagsRegister import FlagsRegister


class Register:
    def __init__(self, name: str, size: int = 32):
        self.name = name
        self.size = size
        self.value = [0] * size
        self.flags = FlagsRegister()

    def load(self, value: int):
        if not (0 <= value <= 2 ** 32 - 1):
            raise ValueError("Value must be between 0 and 2^32-1")


        bits = [int(x) for x in bin(value)[2:]]

        self.value = [0] * (self.size - len(bits)) + bits
        self.flags.update(self.value)

    def to_int(self) -> int:
        return int(''.join(map(str, self.value)), 2)

    def add(self, other: 'Register') -> 'Register':
        sum_val = self.to_int() + other.to_int()
        overflow_occurred = sum_val > (2 ** 32 - 1)


        if overflow_occurred:
            sum_val = sum_val & 0xFFFFFFFF

        self.load(sum_val)
        self.flags.update(self.value, overflow_occurred)
        return self

    def sub(self, other: 'Register') -> 'Register':
        sub_val = self.to_int() - other.to_int()

        if sub_val < 0:
            raise ValueError("Result cannot be negative")

        self.load(sub_val)
        self.flags.update(self.value)
        return self

    def mul(self, other: 'Register') -> 'Register':
        mul_val = self.to_int() * other.to_int()
        overflow_occurred = mul_val > (2 ** 32 - 1)

        if overflow_occurred:
            mul_val = mul_val & 0xFFFFFFFF

        self.load(mul_val)
        self.flags.update(self.value, overflow_occurred)
        return self

    def div(self, other: 'Register') -> 'Register':
        if other.to_int() == 0:
            raise ZeroDivisionError("Division by zero")

        div_val = self.to_int() // other.to_int()
        self.load(div_val)
        self.flags.update(self.value)
        return self

    def __str__(self):
        return f"Register {self.name}: {self.value}, Flags: {self.flags}"