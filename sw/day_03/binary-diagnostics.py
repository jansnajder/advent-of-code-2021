# AoC 2021 - day 3
# Input file shows diagnostics data.
#
# Part 1:  - forward X increases the horizontal position by X units,
#          - down X increases the depth by X units,
#          - up X decreases the depth by X units.
# Part 2:  - down X increases your aim by X units,
#          - up X decreases your aim by X units,
#          - forward X does two things:
#               - It increases your horizontal position by X units.
#               - It increases your depth by your aim multiplied by X.
#
# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you
# multiply your final horizontal position by your final depth?

import copy

from typing import List


def load_data(path: str) -> List[str]:
    '''
    Load input data from filepath

    :param path: inputs file path
    :return binary_numbers: data from the input file
    '''
    with open(path, 'r') as f:
        binary_numbers = f.read().split('\n')

    return binary_numbers


def get_power_consumption(binary_numbers: List[str]) -> int:
    '''
    Get most/least common bits in each position and calculate product of these numbers

    :param binary_numbers: list of input binary number
    :return power_consumption: result power consumption
    '''
    binary_gamma_rate = 0
    binary_epsilon_rate = 0

    for idx in range(len(binary_numbers[0])):
        ones_candidate = 0
        zeros_candidate = 0

        for binary_number in binary_numbers:
            if binary_number[idx] == '1':
                ones_candidate += 1
            elif binary_number[idx] == '0':
                zeros_candidate += 1

        if ones_candidate > zeros_candidate:
            binary_gamma_rate = (binary_gamma_rate << 1) + 1
            binary_epsilon_rate = (binary_epsilon_rate << 1)
        else:
            binary_gamma_rate = (binary_gamma_rate << 1)
            binary_epsilon_rate = (binary_epsilon_rate << 1) + 1

    power_consumption = binary_gamma_rate * binary_epsilon_rate

    return power_consumption


def get_rating(binary_numbers: List[str], idx: int, oxygen: bool) -> List[str]:
    '''
    Get rating of co2 or oxygen according to the specification of the task. This function uses recursion.

    :param binary_number: list of input binary number
    :param idx: index of currently inspected bits
    :param oxygen: indicates if oxygen or co2 is calculated
    :return rating: rating of co2 or oxygen
    '''
    ones_candidate = 0
    zeros_candidate = 0

    ones_indexes = []
    zeros_indexes = []

    for i, binary_number in enumerate(binary_numbers):
        if binary_number[idx] == '1':
            ones_candidate += 1
            ones_indexes.append(i)
        elif binary_number[idx] == '0':
            zeros_candidate += 1
            zeros_indexes.append(i)

    if ones_candidate >= zeros_candidate:
        if oxygen:
            for index in sorted(zeros_indexes, reverse=True):
                binary_numbers.pop(index)
        else:
            for index in sorted(ones_indexes, reverse=True):
                binary_numbers.pop(index)
    else:
        if oxygen:
            for index in sorted(ones_indexes, reverse=True):
                binary_numbers.pop(index)
        else:
            for index in sorted(zeros_indexes, reverse=True):
                binary_numbers.pop(index)

    if len(binary_numbers) > 1:
        binary_numbers = get_rating(binary_numbers, idx + 1, oxygen=oxygen)

    return binary_numbers


if __name__ == '__main__':
    path = 'day_03/inputs.txt'
    binary_numbers = load_data(path)

    power_consumption = get_power_consumption(binary_numbers)
    print(f'Part 1 result: {power_consumption}')

    binary_numbers_copy = copy.deepcopy(binary_numbers)
    oxygen_rating = int(get_rating(binary_numbers, 0, True)[0], 2)
    co2_rating = int(get_rating(binary_numbers_copy, 0, False)[0], 2)
    print(f'Part 2 result: {co2_rating*oxygen_rating}')
