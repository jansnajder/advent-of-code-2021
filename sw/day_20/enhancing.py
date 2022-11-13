def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data_raw = f.read().split('\n\n')
        enhancing_table_raw = data_raw[0]
        image_raw = data_raw[1]

    enhancing_table = enhancing_table_raw.replace('\n', '')
    image = image_raw.split('\n')

    return enhancing_table, image


def scale_image(image, i):
    new_image = []
    if i % 2 == 0:
        sign = '.'
    else:
        sign = '#'
    for row in image:
        new_row = sign + row
        new_row += sign
        new_image.append(new_row)

    len_row = len(new_row)
    blank_line = len_row * sign
    new_image.insert(0, blank_line)
    new_image.append(blank_line)

    return new_image


def enhance(image, enhancing_table, i):
    new_image = []
    lit_count = 0
    for y_idx, row in enumerate(image):
        new_row = ''
        for x_idx, _ in enumerate(row):
            neighbour = get_code(x_idx, y_idx, image, i)
            new_element = get_element(neighbour, enhancing_table)
            if new_element == '#':
                lit_count += 1

            new_row += new_element
        new_image.append(new_row)

    return new_image, lit_count


def get_code(x, y, image, i):
    if i % 2 == 0:
        sign = '.'
    else:
        sign = '#'
    x_list = [x - 1, x, x + 1]
    y_list = [y - 1, y, y + 1]
    neighbour = ''
    for y_c in y_list:
        for x_c in x_list:
            try:
                neighbour += image[y_c][x_c]
            except IndexError:
                neighbour += sign

    return neighbour


def get_element(neighbour, enhancing_table):
    binary_string = ''
    for sign in neighbour:
        if sign == '.':
            binary_string += '0'
        else:
            binary_string += '1'

    index = int(binary_string, 2)

    return enhancing_table[index]


if __name__ == '__main__':
    path = 'inputs.txt'
    enhancing_table, image = load_data(path)

    for i in range(50):
        image = scale_image(image, i)
        image, lit_count = enhance(image, enhancing_table, i)

    print(lit_count)
