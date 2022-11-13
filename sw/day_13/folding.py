def load_data(path):
    with open(path, 'r') as f:
        data_raw = f.read().split('\n')

    data = []
    for line in data_raw:
        data.append((int(line.split(',')[0]), int(line.split(',')[1])))

    return data


def create_map(data):
    x_max = max([i[0] for i in data])
    y_max = max([i[1] for i in data])
    dot_map = [[0 for i in range(x_max + 1)] for j in range(y_max + 1)]

    for row in data:
        dot_map[row[1]][row[0]] = 1

    return dot_map


def fold_map(data, horizontal, line):
    if horizontal:
        idx = 1
    else:
        idx = 0

    for c_idx, coordinate in enumerate(data):
        if coordinate[idx] == line:
            del data[c_idx]
        if coordinate[idx] > line:
            if idx == 1:
                data[c_idx] = (coordinate[0], line * 2 - coordinate[idx])
            if idx == 0:
                data[c_idx] = (line * 2 - coordinate[idx], coordinate[1])

    return data


def print_map(data):
    print('--------------------------------------------------------')
    x_max = max([i[0] for i in data])
    y_max = max([i[1] for i in data])
    dot_map = [['.' for i in range(x_max + 1)] for j in range(y_max + 1)]
    for coordinate in data:
        dot_map[coordinate[1]][coordinate[0]] = '#'

    for row in dot_map:
        print(row)
    print('--------------------------------------------------------')


if __name__ == '__main__':
    test_path = 'test_inputs.txt'
    test_data = load_data(test_path)

    test_data = fold_map(test_data, True, 7)
    test_data = fold_map(test_data, False, 5)
    print_map(test_data)

    path = 'inputs.txt'
    data = load_data(path)

    data = fold_map(data, False, 655)
    data = fold_map(data, True, 447)
    data = fold_map(data, False, 327)
    data = fold_map(data, True, 223)
    data = fold_map(data, False, 163)
    data = fold_map(data, True, 111)
    data = fold_map(data, False, 81)
    data = fold_map(data, True, 55)
    data = fold_map(data, False, 40)
    data = fold_map(data, True, 27)
    data = fold_map(data, True, 13)
    data = fold_map(data, True, 6)
    print_map(data)
