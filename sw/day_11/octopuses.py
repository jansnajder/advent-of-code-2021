from typing import List, Tuple

TEnergy = List[List[int]]


def load_data(path: str) -> TEnergy:
    with open(path, 'r', encoding='utf-8') as f:
        data_raw = f.read().split('\n')

    data = [[int(number) for number in row] for row in data_raw]
    return data


def increase_energy(energy: TEnergy) -> TEnergy:
    new_energy = [list(map(lambda x: x + 1, row)) for row in energy]
    return new_energy


def simulate_flash(energy_levels: TEnergy, row_idx: int, number_idx: int) -> TEnergy:
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
    already_flashed = [[False for number in row] for row in energy]
    height = len(energy)
    done = False

    flashes = 0
    flash_round = True

    while flash_round:
        flash_round = False

        for row_idx in range(height):
            flash_idxs = [i for i, x in enumerate(energy[row_idx]) if x > 9]

            for flash_idx in flash_idxs:
                if not already_flashed[row_idx][flash_idx]:
                    already_flashed[row_idx][flash_idx] = True
                    energy = simulate_flash(energy, row_idx, flash_idx)
                    flashes += 1
                    flash_round = True

    for row_idx in range(height):
        idxs = [i for i, x in enumerate(already_flashed[row_idx]) if x]

        for idx in idxs:
            energy[row_idx][idx] = 0

    return energy, flashes


if __name__ == '__main__':
    path = 'day_11/inputs.txt'
    energy = load_data(path)
    flashes = 0

    for step in range(1000):
        energy = increase_energy(energy)
        energy, new_flashes = find_flashers(energy)

        if new_flashes == 100:
            print(step)
            break

        flashes += new_flashes

    print(flashes)
