import copy


def load_data(path):
    with open(path, 'r') as f:
        data_raw = f.read().split('\n')

    floormap = []
    for line in data_raw:
        floormap.append(list(line))

    return floormap


def move_horizontally(floormap):
    new_floormap = copy.deepcopy(floormap)
    len_row = len(floormap[0])
    moves = 0
    for r_idx, row in enumerate(floormap):
        for e_idx, element in enumerate(row):
            if element != '>':
                continue

            if e_idx == (len_row - 1):
                next_element = 0
            else:
                next_element = e_idx + 1

            if floormap[r_idx][next_element] == '.':
                new_floormap[r_idx][e_idx] = '.'
                new_floormap[r_idx][next_element] = '>'
                moves += 1

    return new_floormap, moves


def move_vertically(floormap, moves):
    new_floormap = copy.deepcopy(floormap)
    len_col = len(floormap)

    for r_idx, row in enumerate(floormap):
        for e_idx, element in enumerate(row):
            if element != 'v':
                continue

            if r_idx == (len_col - 1):
                next_element = 0
            else:
                next_element = r_idx + 1

            if floormap[next_element][e_idx] == '.':
                new_floormap[r_idx][e_idx] = '.'
                new_floormap[next_element][e_idx] = 'v'
                moves += 1

    return new_floormap, moves


if __name__ == '__main__':
    path = 'input.txt'
    floormap = load_data(path)

    moves = 1
    step = 0
    while moves:
        floormap, moves = move_horizontally(floormap)
        floormap, moves = move_vertically(floormap, moves)
        step += 1
        print(f'steps: {step}, moves:{moves}')

print(step)
