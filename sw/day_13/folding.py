# AoC 2021 - day 15
# Input files show coordinates of dots and folding instruction
#
# Part 1:  - Fold the paper once, how many dots are left?
# Part 2:  - Fold the paper according to all instructions and find out the secret code.

from typing import List, Tuple


def load_data(path_coords: str, path_instr: str) -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    '''
    Load data from input files, data consists of coordinates and instructions.

    :param path_coords: path to coordinates file
    :param path_instr: path to instructions file
    :return coords: list of coordinates
    :return instr: list of instructions
    '''
    with open(path_coords, 'r') as f:
        coords_raw = f.read().split('\n')

    coords = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in coords_raw if line]

    with open(path_instr, 'r') as f:
        instr_raw = f.read().split('\n')

    instr = [(line.split('=')[0][-1], int(line.split('=')[1])) for line in instr_raw if line]

    return coords, instr


def fold_paper(coords: List[Tuple[int, int]], axis: str, line: int) -> List[Tuple[int, int]]:
    '''
    Fold paper according to instructions. This results in reduction of coordinates as some mirrors to other.

    :param coords: list of coordinates
    :param axis: identifier of axis of fold
    :param line: line to fold by
    :return coords: list of coordinates after folding
    '''

    if axis == 'x':
        idx = 0
    elif axis == 'y':
        idx = 1
    else:
        raise ValueError(f'Invalid axis identifier "{axis}".')

    for c_idx, coordinate in enumerate(coords):
        if coordinate[idx] == line:
            del coords[c_idx]
        elif coordinate[idx] > line:
            if idx == 1:
                coords[c_idx] = (coordinate[0], line * 2 - coordinate[idx])
            elif idx == 0:
                coords[c_idx] = (line * 2 - coordinate[idx], coordinate[1])

    return list(set(coords))


def print_coords(coords: List[Tuple[int, int]]) -> None:
    '''
    Print coordinates to decode the result.

    :param coords: coordinates of dots
    '''
    print('Result of part two:')
    print('--------------------------------------------------------')
    x_max = max([i[0] for i in coords])
    y_max = max([i[1] for i in coords])
    dot_map = [['.' for i in range(x_max + 1)] for j in range(y_max + 1)]

    for coordinate in coords:
        dot_map[coordinate[1]][coordinate[0]] = '#'

    for row in dot_map:
        print(row)

    print('--------------------------------------------------------')


if __name__ == '__main__':
    path_coords = 'day_13/coordinates.txt'
    path_instr = 'day_13/instructions.txt'
    coords, instructions = load_data(path_coords, path_instr)

    for idx, instr in enumerate(instructions):
        if idx == 1:
            print(f'Result of part one: {len(coords)}')

        coords = fold_paper(coords, instr[0], instr[1])

    print_coords(coords)
