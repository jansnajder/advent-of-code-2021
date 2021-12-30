class Submarine:
    INSTRUCTION_UP = 'up'
    INSTRUCTION_DOWN = 'down'
    INSTRUCTION_FORWARD = 'forward'

    def __init__(self):
        self.instructions = []
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def move_no_aim(self):
        '''Moves according to part one'''
        for instruction in self.instructions:
            steps = int(instruction.split(' ')[1])
            if self.INSTRUCTION_DOWN in instruction:
                self.depth += steps
            elif self.INSTRUCTION_UP in instruction:
                self.depth -= steps
            elif self.INSTRUCTION_FORWARD in instruction:
                self.horizontal += steps

    def move_with_aim(self):
        '''Moves according to part two'''
        for instruction in self.instructions:
            steps = int(instruction.split(' ')[1])
            if self.INSTRUCTION_DOWN in instruction:
                self.aim += steps
            elif self.INSTRUCTION_UP in instruction:
                self.aim -= steps
            elif self.INSTRUCTION_FORWARD in instruction:
                self.horizontal += steps
                self.depth += self.aim * steps

    def reset_position(self):
        '''Reset position variables'''
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def load_instructions(self, path):
        '''
        Loads input data from filepath

        :param path:    file path string
        :return data:   data from the input file
        '''
        with open(path, 'r', encoding='utf-8') as f:
            self.instructions = f.read().split('\n')


if __name__ == '__main__':
    path = 'inputs.txt'
    submarine = Submarine()
    submarine.load_instructions(path)
    submarine.move_no_aim()
    print(f'Part 1 result: {submarine.depth*submarine.horizontal}')

    submarine.reset_position()
    submarine.move_with_aim()
    print(f'Part 2 result: {submarine.depth*submarine.horizontal}')
