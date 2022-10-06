# AoC 2021 - day 7
# Input file shows positions of crabs
#
# Part 1:  - each change of position costs 1 fuel
# Part 2:  - the cost increases with each change of position
#
#           Find the common position for the crab population, which requires
#           the least usage of fuel.

from typing import List


def load_data(path: str) -> List[int]:
    '''
    Load data from input txt file

    :param path: path to input file
    :return positions: list of crab positions
    '''
    with open(path, 'r', encoding='utf-8') as f:
        positions = list(map(int, f.read().split(',')))

    return positions


def get_target_position_same_cost(positions: List[int]) -> int:
    '''
    Get target position in case each consecutive movement has same cost

    :param positions: list of crab positions
    :return target: common position with the lowest fuel cost
    '''
    fuel_costs = [0 for k in range(min(positions), max(positions) + 1)]

    for idx in range(min(positions), max(positions) + 1):
        for position in positions:
            fuel_costs[idx] += abs(position - idx)

    return min(fuel_costs)


def get_target_position_increasing_cost(positions: List[int]) -> int:
    '''
    Get target position in case each consecutive movement has increasing cost

    :param positions: list of crab positions
    :return target: common position with the lowest fuel cost
    '''
    fuel_costs = [0 for k in range(min(positions), max(positions) + 1)]

    for idx in range(min(positions), max(positions) + 1):
        for position in positions:
            distance = abs(position - idx)
            fuel_costs[idx] += int((distance**2 + distance) / 2)

    return min(fuel_costs)


if __name__ == '__main__':
    path = 'day_07/inputs.txt'
    positions = load_data(path)

    target = get_target_position_same_cost(positions)
    print(f'Result of part 1: {target}')

    target = get_target_position_increasing_cost(positions)
    print(f'Result of part 2: {target}')
