from collections import OrderedDict


def get_ops(a, b, c, idx):
    if idx == 0:
        res = [a, b, c]
    elif idx == 1:
        res = [a, c, b]
    elif idx == 2:
        res = [b, a, c]
    elif idx == 3:
        res = [b, c, a]
    elif idx == 4:
        res = [c, a, b]
    elif idx == 5:
        res = [c, b, a]
    elif idx == 6:
        res = [-a, b, c]
    elif idx == 7:
        res = [-a, c, b]
    elif idx == 8:
        res = [-b, a, c]
    elif idx == 9:
        res = [-b, c, a]
    elif idx == 10:
        res = [-c, a, b]
    elif idx == 11:
        res = [-c, b, a]
    elif idx == 12:
        res = [a, -b, c]
    elif idx == 13:
        res = [a, -c, b]
    elif idx == 14:
        res = [b, -a, c]
    elif idx == 15:
        res = [b, -c, a]
    elif idx == 16:
        res = [c, -a, b]
    elif idx == 17:
        res = [c, -b, a]
    elif idx == 18:
        res = [a, b, -c]
    elif idx == 19:
        res = [a, c, -b]
    elif idx == 20:
        res = [b, a, -c]
    elif idx == 21:
        res = [b, c, -a]
    elif idx == 22:
        res = [c, a, -b]
    elif idx == 23:
        res = [c, b, -a]
    elif idx == 24:
        res = [-a, -b, c]
    elif idx == 25:
        res = [-a, -c, b]
    elif idx == 26:
        res = [-b, -a, c]
    elif idx == 27:
        res = [-b, -c, a]
    elif idx == 28:
        res = [-c, -a, b]
    elif idx == 29:
        res = [-c, -b, a]
    elif idx == 30:
        res = [-a, b, -c]
    elif idx == 31:
        res = [-a, c, -b]
    elif idx == 32:
        res = [-b, a, -c]
    elif idx == 33:
        res = [-b, c, -a]
    elif idx == 34:
        res = [-c, a, -b]
    elif idx == 35:
        res = [-c, b, -a]
    elif idx == 36:
        res = [a, -b, -c]
    elif idx == 37:
        res = [a, -c, -b]
    elif idx == 38:
        res = [b, -a, -c]
    elif idx == 39:
        res = [b, -c, -a]
    elif idx == 40:
        res = [c, -a, -b]
    elif idx == 41:
        res = [c, -b, -a]
    elif idx == 42:
        res = [-a, -b, -c]
    elif idx == 43:
        res = [-a, -c, -b]
    elif idx == 44:
        res = [-b, -a, -c]
    elif idx == 45:
        res = [-b, -c, -a]
    elif idx == 46:
        res = [-c, -a, -b]
    elif idx == 47:
        res = [-c, -b, -a]

    return res


def get_op(a, b, c, idx):
    if idx == 0:
        res = [a, b, c]
    elif idx == 1:
        res = [a, c, -b]
    elif idx == 2:
        res = [a, -b, -c]
    elif idx == 3:
        res = [a, -c, b]
    elif idx == 4:
        res = [-a, -b, c]
    elif idx == 5:
        res = [-a, c, b]
    elif idx == 6:
        res = [-a, b, -c]
    elif idx == 7:
        res = [-a, -c, -b]
    elif idx == 8:
        res = [b, c, a]
    elif idx == 9:
        res = [b, a, -c]
    elif idx == 10:
        res = [b, -c, -a]
    elif idx == 11:
        res = [b, -a, c]
    elif idx == 12:
        res = [-b, -c, a]
    elif idx == 13:
        res = [-b, a, c]
    elif idx == 14:
        res = [-b, c, -a]
    elif idx == 15:
        res = [-b, -a, -c]
    elif idx == 16:
        res = [c, a, b]
    elif idx == 17:
        res = [c, b, -a]
    elif idx == 18:
        res = [c, -a, -b]
    elif idx == 19:
        res = [c, -b, a]
    elif idx == 20:
        res = [-c, -a, b]
    elif idx == 21:
        res = [-c, b, a]
    elif idx == 22:
        res = [-c, a, -b]
    elif idx == 23:
        res = [-c, -b, -a]

    return res


def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data_raw = f.read().split('\n')

    coordinates_raw = []
    coordinates = []
    for line in data_raw:
        if line:
            coordinates_raw.append(tuple(map(int, line.split(','))))
        else:
            coordinates.append(coordinates_raw)
            coordinates_raw = []

    return coordinates


path = 'inputs.txt'
coordinates = load_data(path)
baseline = coordinates.pop(0)
baseline_diffs = []
baseline_indexes = []

for idx_0 in range(len(baseline) - 1):
    for idx_1 in range(idx_0 + 1, len(baseline)):
        diffs = [baseline[idx_1][i] - baseline[idx_0][i] for i in range(3)]
        baseline_diffs.append(diffs)
        indexes = (idx_1, idx_0)
        baseline_indexes.append(indexes)

scanner_locations = [(0, 0, 0)]
while len(coordinates):
    # for idx_0 in range(len(baseline)-1):
    # 	for idx_1 in range(idx_0+1, len(baseline)):
    # 		diffs = [baseline[idx_1][i] - baseline[idx_0][i] for i in range(3)]
    # 		baseline_diffs.append(diffs)
    # 		indexes = (idx_1, idx_0)
    # 		baseline_indexes.append(indexes)

    target = coordinates.pop(0)
    ops = [0 for x in range(24)]
    tr = None

    for idx_0 in range(len(target) - 1):
        for idx_1 in range(idx_0 + 1, len(target)):
            a0 = target[idx_0][0]
            b0 = target[idx_0][1]
            c0 = target[idx_0][2]
            a1 = target[idx_1][0]
            b1 = target[idx_1][1]
            c1 = target[idx_1][2]
            for i in range(24):
                coordinate_0 = get_op(a0, b0, c0, i)
                coordinate_1 = get_op(a1, b1, c1, i)
                diff = [coordinate_1[j] - coordinate_0[j] for j in range(3)]
                if diff in baseline_diffs:
                    ops[i] += 1
                    if ops[i] == 4:
                        index = baseline_diffs.index(diff)
                        common = [baseline[baseline_indexes[index][1]]]
                        common.append(coordinate_0)
                        tr = i
                        offset = [common[1][i] - common[0][i] for i in range(3)]
                        scanner_locations.append(tuple(offset))
                        break
            if tr is not None:
                break
        if tr is not None:
            break

    if tr:
        #print(tr)
        orig_len = len(baseline)
        morphed_list = []
        for element in target:
            morphed = get_op(element[0], element[1], element[2], tr)
            morphed = [morphed[i] - offset[i] for i in range(3)]
            morphed = tuple(map(int, morphed))
            if morphed not in baseline:
                baseline.append(morphed)

        for idx_0 in range(orig_len, len(baseline) - 1):
            for idx_1 in range(idx_0 + 1, len(baseline)):
                diffs = [baseline[idx_1][i] - baseline[idx_0][i] for i in range(3)]
                baseline_diffs.append(diffs)
                indexes = (idx_1, idx_0)
                baseline_indexes.append(indexes)

    else:
        coordinates.append(target)

print(len(set(baseline)))
print(scanner_locations)


def manhattan(loc_1, loc_2):
    result = 0
    for i in range(3):
        result += abs(loc_1[i] - loc_2[i])

    return result


res = 0
for idx_0 in range(len(scanner_locations) - 1):
    for idx_1 in range(idx_0 + 1, len(scanner_locations)):
        res = max(res, manhattan(scanner_locations[idx_0], scanner_locations[idx_1]))

print(res)
