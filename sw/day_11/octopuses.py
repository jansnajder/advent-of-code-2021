def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data_raw = f.read().split('\n')

    data = []
    for row in data_raw:
        row_numbers = []
        for number in row:
            row_numbers.append(int(number))
        data.append(row_numbers)

    return data


def increase_energy(energy):
    new_energy = []

    for row in energy:
        new_row = list(map(lambda x: x + 1, row))
        new_energy.append(new_row)

    return new_energy


def simulate_flash(energy_levels, row_idx, number_idx):
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


def find_flashers(energy):
    already_flashed = [[0 for number in row] for row in energy]
    height = len(energy)
    done = False

    flashes = 0
    while not done:
        flash_round = 0
        for row_idx in range(height):
            flash_idxs = [i for i, x in enumerate(energy[row_idx]) if x > 9]
            if flash_idxs:
                for flash_idx in flash_idxs:
                    if already_flashed[row_idx][flash_idx] == 0:
                        already_flashed[row_idx][flash_idx] += 1
                        energy = simulate_flash(energy, row_idx, flash_idx)
                        flash_round += 1

        flashes += flash_round
        if flash_round == 0:
            done = True

    for row_idx in range(height):
        idxs = [i for i, x in enumerate(already_flashed[row_idx]) if x > 0]
        for idx in idxs:
            energy[row_idx][idx] = 0

    return energy, flashes


if __name__ == '__main__':
    test_path = 'test_inputs.txt'
    test_energy = load_data(test_path)

    flashes = 0
    for step in range(100):
        test_energy = increase_energy(test_energy)
        test_energy, new_flashes = find_flashers(test_energy)
        flashes += new_flashes

    assert flashes == 1656

    path = 'inputs.txt'
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
