# AoC 2021 - day 1
# Input file shows sonar depth measurements.
#
# Part 1: How many measurements are larger than the previous measurement?
# Part 2: Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

from typing import List


def load_data(path: str) -> List[int]:
    '''
    Load input data from filepath

    :param path: file path string
    :return data: data from the input file
    '''
    with open(path, 'r') as f:
        data = list(map(int, f.read().split('\n')))

    return data

def count_increments(data: List[int]) -> int:
    '''
    Count elements which increased compared to the previous element

    :param data:  list with numbers
    :return increasing: number of increasing elements
    '''
    increasing = 0

    for idx, number in enumerate(data):
        if idx > 0 and number > int(data[idx-1]):
            increasing += 1

    return increasing


def sliding_window(data: List[int], window_length: int) -> int:
    '''
    Create list of sums by going through the input list with sliding window. Call count_increments on the newly
    created list.

    :param data: list with numbers
    :param window_length: length of sliding window
    :return increasing: number of increasing elements
    '''
    windows = []
    sliding = 0

    for idx in range(len(data) - (window_length - 1)):
        for k in range(window_length):
            sliding += int(data[idx + k])

        windows.append(sliding)
        sliding = 0

    increasing = count_increments(windows)

    return increasing


if __name__ == '__main__':
    path = 'day_01/inputs.txt'
    data = load_data(path)
    print(f'Part 1 result: {count_increments(data)}')
    print(f'Part 2 result: {sliding_window(data, 3)}')