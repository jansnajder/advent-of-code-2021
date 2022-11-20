# AoC 2021 - day 2
# Input file shows instructions to the submarine.
#
# Part 1: Each bit in the gamma/epsilon rate can be determined by finding the most/least common bit in the corresponding
#         position of all numbers in the diagnostic report.
#
#         Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply
#         them together. What is the power consumption of the submarine?
# Part 2:  - To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and
#            keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in
#             the position being considered.
#          - To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and
#            keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in
#            the position being considered.
#
# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating,
# then multiply them together. What is the life support rating of the submarine?

from typing import List


class Submarine:
    '''
    Class representing submarine.

    :param path: path to input files
    '''
    # Instructions definition
    INSTRUCTION_UP = 'up'
    INSTRUCTION_DOWN = 'down'
    INSTRUCTION_FORWARD = 'forward'

    def __init__(self, path: str):
        self.instructions = self.load_instructions(path)
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def move_no_aim(self) -> None:
        '''Move according to part one.'''
        for instruction in self.instructions:
            steps = int(instruction.split(' ')[1])

            if self.INSTRUCTION_DOWN in instruction:
                self.depth += steps
            elif self.INSTRUCTION_UP in instruction:
                self.depth -= steps
            elif self.INSTRUCTION_FORWARD in instruction:
                self.horizontal += steps

    def move_with_aim(self) -> None:
        '''Move according to part two.'''
        for instruction in self.instructions:
            steps = int(instruction.split(' ')[1])

            if self.INSTRUCTION_DOWN in instruction:
                self.aim += steps
            elif self.INSTRUCTION_UP in instruction:
                self.aim -= steps
            elif self.INSTRUCTION_FORWARD in instruction:
                self.horizontal += steps
                self.depth += self.aim * steps

    def reset_position(self) -> None:
        '''Reset position variables.'''
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def load_instructions(self, path: str) -> List[str]:
        '''
        Load input data from filepath

        :param path: input file path
        '''
        with open(path, 'r', encoding='utf-8') as f:
            instructions = f.read().split('\n')

        return instructions


if __name__ == '__main__':
    path = 'day_02/inputs.txt'
    submarine = Submarine(path)
    submarine.move_no_aim()
    print(f'Part 1 result: {submarine.depth*submarine.horizontal}')

    submarine.reset_position()
    submarine.move_with_aim()
    print(f'Part 2 result: {submarine.depth*submarine.horizontal}')
