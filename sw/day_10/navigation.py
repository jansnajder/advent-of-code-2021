# AoC 2021 - day 10
# Input file shows navigation lines.
#
# Part 1:  - find value of illegal character - character which does not comply
#            to the opening sequence. Result is sum of these values.
# Part 2:  - find missing closing sequence

from typing import List


def load_data(path: str) -> List[str]:
    '''
    Load navigation lines data.

    :param path: path to txt file
    :return nav_lines: list of navigation lines
    '''
    with open(path, 'r', encoding='utf-8') as f:
        nav_lines = f.read().split('\n')

    return nav_lines


def get_illegal_char(nav_line: str) -> int:
    '''
    Get the character which breaks the closing pattern.

    :param nav_line: navigation line
    :return value: result value of the illegal character
    '''
    OPENING = ['(', '[', '{', '<']
    CLOSING = [')', ']', '}', '>']
    results = {'None': 0, ')': 3, ']': 57, '}': 1197, '>': 25137}
    illegal = 'None'
    opening_list = []

    for char in nav_line:
        if char in OPENING:
            opening_list.append(OPENING.index(char))
        elif char in CLOSING:
            if CLOSING.index(char) == opening_list[-1]:
                del opening_list[-1]
            else:
                illegal = char
                break

    return results[illegal]


def get_closing_sequence(nav_line: str) -> int:
    '''
    Get value of closing sequence of navigation line.

    :param nav_line: navigation line
    :return result: value of closing sequence
    '''
    OPENING = ['(', '[', '{', '<']
    CLOSING = [')', ']', '}', '>']
    opening_list = []

    for char in nav_line:
        if char in OPENING:
            opening_list.append(OPENING.index(char))
        elif char in CLOSING:
            del opening_list[-1]

    result = 0

    for idx in range(len(opening_list), 0, -1):
        result *= 5
        result += opening_list[idx - 1] + 1

    return result


if __name__ == '__main__':
    path = 'day_10/inputs.txt'
    nav_lines = load_data(path)

    result_part_one = 0
    incomplete_nav_lines = []

    for nav_line in nav_lines:
        score = get_illegal_char(nav_line)
        result_part_one += score

        if score == 0:
            incomplete_nav_lines.append(nav_line)

    print(f'Result of part one: {result_part_one}')

    res = []

    for nav_line in incomplete_nav_lines:
        res.append(get_closing_sequence(nav_line))

    idx_of_result = int(len(res) / 2)
    result_part_two = sorted(res)[idx_of_result]

    print(f'Result of part two: {result_part_two}')
