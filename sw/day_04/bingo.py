# AoC 2021 - day 4
# Input file shows bingo boards and bingo inputs
#
# Part 1: Figure out which board will win first. Calculate the final score by multiplying sum of all unmarked numbers
#         with the input number, which caused the board to win. What will be the final score?
# Part 2: Figure out which board will win last. Calculate the final score by multiplying sum of all unmarked numbers
#         with the input number, which caused the board to win. What will be the final score?

import numpy as np

from typing import List, Tuple, TypeVar


class BingoBoard:
    '''
    Class representing board of bingo numbers

    :param raw board: 2D np array representing numbers in bingo board
    '''

    def __init__(self, raw_board: np.ndarray):
        self.board = raw_board
        self.won: bool = False

    def mark_number(self, input: int) -> None:
        '''
        Check bingo board and mark the position of input if present.

        :param input: bingo input
        '''
        if self.won is True:
            return

        self.board = np.where(self.board != input, self.board, -1)

    def has_won(self) -> bool:
        '''
        Check if the board has won.

        :return: bool indicating if the board already won
        '''
        if (-5 in np.sum(self.board, axis=0)) or (-5 in np.sum(self.board, axis=-1)):
            self.won = True

        return self.won


def load_data(inputs_path: str, bingo_path: str) -> Tuple[List[int], List[np.ndarray]]:
    '''
    Load bingo boards and bing inputs

    :param inputs_path: path to bing inputs
    :param bingo_path: path to bingo boards
    :return inputs: parsed bingo inputs
    :return bingo: parsed bingo boards
    '''
    with open(inputs_path, 'r', encoding='utf-8') as f:
        inputs_raw = f.read().split(',')
        inputs = list(map(int, inputs_raw))

    with open(bingo_path, 'r', encoding='utf-8') as f:
        bingo_raw = f.read().split('\n\n')

    bingo: List[np.ndarray] = []

    for value in bingo_raw:
        bingo.append(np.fromstring(value, dtype=int, sep=' ').reshape((5, 5)))

    return inputs, bingo


def get_result(bingo_board: BingoBoard, input: int) -> int:
    '''
    Get result for given bingo board and its winning input.

    :param bingo_board: winning bingo board
    :param input: winning bing input
    :return: result of the task
    '''
    sum = 0

    for row in bingo_board.board:
        for number in row:
            if number > 0:
                sum += number

    return sum * input


if __name__ == '__main__':
    inputs_path = 'day_04/inputs.txt'
    bingo_path = 'day_04/bingo_boards.txt'
    inputs, bingo_raw = load_data(inputs_path, bingo_path)

    bingo_boards: List[BingoBoard] = []

    for bingo in bingo_raw:
        bingo_boards.append(BingoBoard(bingo))

    winners = []

    for input in inputs:
        for board in bingo_boards:
            board.mark_number(input)

            if not board.won:
                win = board.has_won()

                if win:
                    winners.append((board, input))

    print(f'Part 1 result: {get_result(winners[0][0], winners[0][1])}')
    print(f'Part 2 result: {get_result(winners[-1][0], winners[-1][1])}')
