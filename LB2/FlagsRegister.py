class FlagsRegister:
    def __init__(self):
        self.zero = False
        self.negative = False
        self.overflow = False

    def update(self, value: list, overflow_occurred: bool = False):

        self.zero = all(bit == 0 for bit in value)


        self.negative = False


        self.overflow = overflow_occurred

    def __str__(self):
        return f"Z: {int(self.zero)}, N: {int(self.negative)}, O: {int(self.overflow)}"
