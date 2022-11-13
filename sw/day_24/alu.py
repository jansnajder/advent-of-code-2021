class Instruction:

    def __init__(self, operation, address, argument=None):
        self.operation = operation
        self.address = address
        self.argument = argument


class ALU:

    def __init__(self):
        self.values = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def run_instruction(self, instruction):
        operation = instruction.operation

        if operation == 'inp':
            self.op_input(instruction)
        elif operation == 'add':
            self.op_add(instruction)
        elif operation == 'mul':
            self.op_mul(instruction)
        elif operation == 'div':
            self.op_div(instruction)
        elif operation == 'mod':
            self.op_mod(instruction)
        elif operation == 'eql':
            self.op_equal(instruction)
        else:
            raise ValueError

    def op_input(self, instruction):
        self.values[instruction.address] = instruction.argument

    def op_add(self, instruction):
        try:
            self.values[instruction.address] += self.values[instruction.argument]
        except KeyError:
            self.values[instruction.address] += int(instruction.argument)

    def op_mul(self, instruction):
        try:
            self.values[instruction.address] *= self.values[instruction.argument]
        except KeyError:
            self.values[instruction.address] *= int(instruction.argument)

    def op_div(self, instruction):
        try:
            self.values[instruction.address] //= self.values[instruction.argument]
        except KeyError:
            self.values[instruction.address] //= int(instruction.argument)

    def op_mod(self, instruction):
        try:
            self.values[instruction.address] %= self.values[instruction.argument]
        except KeyError:
            self.values[instruction.address] %= int(instruction.argument)

    def op_equal(self, instruction):
        try:
            if self.values[instruction.address] == self.values[instruction.argument]:
                self.values[instruction.address] = 1
            else:
                self.values[instruction.address] = 0
        except KeyError:
            if self.values[instruction.address] == int(instruction.argument):
                self.values[instruction.address] = 1
            else:
                self.values[instruction.address] = 0


def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        instructions_raw = f.read().split('\n')

    instructions = []
    for line in instructions_raw:
        parts = line.split(' ')
        if len(parts) == 2:
            instructions.append(Instruction(parts[0], parts[1]))
        else:
            instructions.append(Instruction(parts[0], parts[1], argument=parts[2]))

    return instructions


if __name__ == '__main__':
    path = 'inputs.txt'
    instructions = load_data(path)

    alu = ALU()
    for instruction in instructions:
        if instruction.operation == 'inp':
            instruction.argument = 9
        alu.run_instruction(instruction)

print(alu.values)
