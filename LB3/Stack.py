from Register import Register


class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass


class Stack:
    def __init__(self, size=8):
        self.size = size
        self.registers = [Register(f"r{i}") for i in range(size)]
        self.sp = 0  # Stack pointer

    def push(self, value):
        if self.is_full():
            raise StackOverflow("Stack overflow")
        self.registers[self.sp].load(value)
        self.registers[self.sp].flags.update(self.registers[self.sp].value)
        self.sp += 1

    def pop(self):
        if self.is_empty():
            raise StackUnderflow("Stack underflow")
        self.sp -= 1
        value = self.registers[self.sp].to_int()
        self.registers[self.sp].flags.update(self.registers[self.sp].value)
        return value

    def is_empty(self):
        return self.sp == 0

    def is_full(self):
        return self.sp == self.size

    def clear(self):
        self.sp = 0
        for reg in self.registers:
            reg.load(0)
            reg.flags.update(reg.value)
