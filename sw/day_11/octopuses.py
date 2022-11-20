# AoC 2021 - day 11
# Input file show energy level grid.
#
# In each round energy level of the grid raises by one, if any energy level is 9 or higher, it flashes, raising level of
# neighboring energy levels and resets to zero. During round each level can flash only once.
#
# Part 1:  - How many flashes is there after 100 steps?
# Part 2:  - When is the first moment of synchronized flashing?

from typing import List, Tuple

TEnergy = List[List[int]]


def load_data(path: str) -> TEnergy:
    '''
    Load data from input path. Data represents grid of energy levels.

    :param path: path of input data
    :return data: energy grid in form of list of lists of integers
    '''
    with open(path, 'r', encoding='utf-8') as f:
        data_raw = f.read().split('\n')

    data = [[int(number) for number in row] for row in data_raw]
    return data


def increase_energy(energy: TEnergy) -> TEnergy:
    '''
    Increase energy of the grid.

    :param energy: original energy grid
    :return new_energy: energy grid after increasing
    '''
    new_energy = [list(map(lambda x: x + 1, row)) for row in energy]
    return new_energy


def simulate_flash(energy_levels: TEnergy, row_idx: int, number_idx: int) -> TEnergy:
    '''
    Simulate flash of octopus on given location. Flash makes energy of neighboring octopuses raise by one.

    :param energy_levels: energy grid
    :param row_idx: index of row
    :param number_idx: index of column
    :return energy_levels: energy grid after flash on given coordinates
    '''
    low_boundary = 0
    high_boundary = 9

    upper_ok = False
    lower_ok = False

    if (number_idx - 1) >= low_boundary:
        lower_ok = True
        energy_levels[row_idx][number_idx - 1] += 1

    if (number_idx + 1) <= high_boundary:
        upper_ok = True
        energy_levels[row_idx][number_idx + 1] += 1

    if (row_idx - 1) >= low_boundary:
        energy_levels[row_idx - 1][number_idx] += 1

        if lower_ok:
            energy_levels[row_idx - 1][number_idx - 1] += 1
        if upper_ok:
            energy_levels[row_idx - 1][number_idx + 1] += 1

    if (row_idx + 1) <= high_boundary:
        energy_levels[row_idx + 1][number_idx] += 1

        if lower_ok:
            energy_levels[row_idx + 1][number_idx - 1] += 1
        if upper_ok:
            energy_levels[row_idx + 1][number_idx + 1] += 1

    return energy_levels


def find_flashers(energy: TEnergy) -> Tuple[TEnergy, int]:
    '''
    Find octopuses, which are about to flash. Do the flashing (it can chain), count number of flashes.

    :param energy: energy grid
    :return energy: energy grid after flashing
    :return flashes: number of flashed octopuses in  this round
    '''
    already_flashed = [[False for number in row] for row in energy]
    flashes = 0
    did_flash = True

    while did_flash:
        did_flash = False

        for row_idx, row in enumerate(energy):
            flash_indexes = [i for i, x in enumerate(row) if x > 9]

            for col_idx in flash_indexes:
                if not already_flashed[row_idx][col_idx]:
                    already_flashed[row_idx][col_idx] = True
                    energy = simulate_flash(energy, row_idx, col_idx)
                    flashes += 1
                    did_flash = True

    for row_idx, row in enumerate(energy):
        energy[row_idx] = [0 if already_flashed[row_idx][col_idx] else value for col_idx, value in enumerate(row)]

    return energy, flashes


if __name__ == '__main__':
    path = 'day_11/inputs.txt'
    energy = load_data(path)
    flashes = 0

    for step in range(1000):
        energy = increase_energy(energy)
        energy, new_flashes = find_flashers(energy)

        # synchronized flashing means all flashed during one round, i.e 100 flashes
        if new_flashes == 100:
            print(f'Result of part two: {step + 1}')
            break

        flashes += new_flashes

        if (step + 1) == 100:
            print(f'Result of part one: {flashes}')
