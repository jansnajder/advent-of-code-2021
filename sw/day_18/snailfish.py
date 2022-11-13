def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')

    processed = []
    for line in data:
        depth = 0
        processed_line = []
        for idx, element in enumerate(line):
            if element == '[':
                depth += 1
            elif element == ']':
                depth -= 1
            elif element == ',':
                pass
            else:
                processed_line.append([int(element), depth])
        processed.append(processed_line)

    return processed


if __name__ == '__main__':
    path = 'test_sum.txt'
    data = load_data(path)
    sum = []
    # for line in data:
    #     if not sum:
    #         sum = line
    #     else:
    #         sum += line
    #         sum = [[element[0], element[1]+1] for element in sum]

    #     updated = True
    #     while updated:
    #         updated = False
    #         for idx, element in enumerate(sum):
    #             if element[1] > 4:
    #                 if idx > 0:
    #                     sum[idx][0] +=
