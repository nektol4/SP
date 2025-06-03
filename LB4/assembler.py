from register import Register
from stack import Stack


class AssemblerCommands:
    def __init__(self):
        self.registers = {}
        self.stack = None

    def mov(self, dest, src):
        if isinstance(src, int):
            self.registers[dest].load(src)
        else:
            self.registers[dest].load(self.registers[src].to_int())

    def add(self, dest, src):
        if isinstance(src, int):
            reg_src = Register("temp")
            reg_src.load(src)
            self.registers[dest].add(reg_src)
        else:
            self.registers[dest].add(self.registers[src])

    def sub(self, dest, src):
        if isinstance(src, int):
            reg_src = Register("temp")
            reg_src.load(src)
            self.registers[dest].sub(reg_src)
        else:
            self.registers[dest].sub(self.registers[src])

    def cmp(self, op1, op2):
        reg1 = Register("cmp1")
        reg2 = Register("cmp2")
        reg1.load(self.registers[op1].to_int() if isinstance(op1, str) else op1)
        reg2.load(self.registers[op2].to_int() if isinstance(op2, str) else op2)
        result = reg1.to_int() - reg2.to_int()
        reg1._update_flags_and_set_value(result)
        self.registers[op1].flags = reg1.flags

    def push(self, value):
        if isinstance(value, int):
            self.stack.push(value)
        else:
            self.stack.push(self.registers[value].to_int())

    def pop(self, dest):
        value = self.stack.pop()
        self.registers[dest].load(value)
