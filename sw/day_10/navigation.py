def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        nav_lines = f.read().split('\n')

    return nav_lines


def get_illegal_char(nav_line):
    OPENING = ['(', '[', '{', '<']
    CLOSING = [')', ']', '}', '>']
    RESULTS = {'None': 0, ')': 3, ']': 57, '}': 1197, '>': 25137}

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

    return RESULTS[illegal]


def get_closing_sequence(nav_line):
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
    # test part 1
    test_path = 'test_inputs.txt'
    test_nav_lines = load_data(test_path)
    test_result_1 = 0
    test_incomplete_nav_lines = []

    for test_nav_line in test_nav_lines:
        score = get_illegal_char(test_nav_line)
        test_result_1 += score
        if score == 0:
            test_incomplete_nav_lines.append(test_nav_line)

    assert test_result_1 == 26397

    # real part 1
    path = 'inputs.txt'
    nav_lines = load_data(path)
    result_1 = 0
    incomplete_nav_lines = []

    for nav_line in nav_lines:
        score = get_illegal_char(nav_line)
        result_1 += score
        if score == 0:
            incomplete_nav_lines.append(nav_line)

    print(result_1)

    # test part 2
    test_results_2 = []
    for test_nav_line in test_incomplete_nav_lines:
        test_results_2.append(get_closing_sequence(test_nav_line))

    assert test_results_2 == [288957, 5566, 1480781, 995444, 294]

    test_idx_of_result = int(len(test_results_2) / 2)
    test_result_2 = sorted(test_results_2)[test_idx_of_result]

    assert test_result_2 == 288957

    # real part 2
    results_2 = []
    for nav_line in incomplete_nav_lines:
        results_2.append(get_closing_sequence(nav_line))

    idx_of_result = int(len(results_2) / 2)
    result_2 = sorted(results_2)[idx_of_result]

    print(result_2)
