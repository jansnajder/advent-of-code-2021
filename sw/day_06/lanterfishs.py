# AoC 2021 - day 6
# Input file shows initial ages of lantern-fishes.
# 
# Lantern-fish with an internal timer value of 3:
# 
#   - After one day, its internal timer would become 2.
#   - After another day, its internal timer would become 1.
#   - After another day, its internal timer would become 0.
#   - After another day, its internal timer would reset to 6, and it would 
#     create a new lantern-fish with an internal timer of 8.
#   - After another day, the first lantern-fish would have an internal timer
#     of 5, and the second lantern-fish would have an internal timer of 7.
#
# Part 1:  - How many lantern-fishes will be there after 80 days?
# Part 2:  - How many lantern-fishes will be there after 256 days?

from typing import List


def load_data(path: str) -> List[int]:
    '''
    Load input data.

    :param path:path to input txt file
    :return ages: list of fish ages
    '''
    with open(path, 'r', encoding='utf-8') as f:
        ages_raw = f.read()

    ages = list(map(int, ages_raw.strip('\n').split(',')))

    return ages


if __name__ == '__main__':
    path = 'day_06/inputs.txt'
    fish_ages = load_data(path)
    ages = [0] * 9

    for age in fish_ages:
        ages[age] += 1

    for day in range(256):
        if day == 80:
            print(f'Result Part 1: {sum(ages)}.')

        cycle = ages[0]

        for age in range(1, len(ages)):
            ages[age - 1] = ages[age]

        ages[6] += cycle
        ages[8] = cycle

    print(f'Result Part 2: {sum(ages)}.')
