import copy

def load_data(path):
    '''
    Loads input data from filepath

    :param path:    file path string
    :return data:   data from the input file
    '''
    with open(path, 'r') as f:
        bitnumbers = f.read().split('\n')

    return bitnumbers

def get_power_consumption(binary_numbers):
    '''
    Gets most/least common bits in each position and calculate product of these numbers

    :param binary_number:       list of input binary number
    :return power_consumption:  int
    '''
    binary_gamma_rate = ''
    binary_epsilon_rate = ''

    for idx, _ in enumerate(binary_numbers[0]):
        ones_candidate = 0
        zeros_candidate = 0

        for binary_number in binary_numbers:
            if binary_number[idx] == '1':
                ones_candidate += 1
            elif binary_number[idx] == '0':
                zeros_candidate += 1

        if ones_candidate > zeros_candidate:
            binary_gamma_rate += '1'
            binary_epsilon_rate += '0'
        else:
            binary_gamma_rate += '0'
            binary_epsilon_rate += '1'

    power_consumption = int(binary_gamma_rate, 2) * int(binary_epsilon_rate, 2)

    return power_consumption


def get_rating(binary_numbers, idx, oxygen=True):
    '''
    Gets most/least common bits in each position and calculate product of these numbers

    :param binary_number:   list of input binary number
    :param idx:             int bit index
    :param oxygen:          bool to calc oxygen of co2
    :return oxygen          or co2 rating: int
    '''

    ones_candidate = 0
    zeros_candidate = 0

    ones_indexes = []
    zeros_indexes = []

    for i, binary_number in enumerate(binary_numbers):
        if binary_number[idx] == '1':
            ones_candidate += 1
            ones_indexes.append(i)
        elif binary_number[idx] == '0':
            zeros_candidate += 1
            zeros_indexes.append(i)

    if ones_candidate >= zeros_candidate:
        if oxygen:
            for index in sorted(zeros_indexes, reverse=True):
                binary_numbers.pop(index)
        else:
            for index in sorted(ones_indexes, reverse=True):
                binary_numbers.pop(index)
    else:
        if oxygen:
            for index in sorted(ones_indexes, reverse=True):
                binary_numbers.pop(index)
        else:
            for index in sorted(zeros_indexes, reverse=True):
                binary_numbers.pop(index)

    if len(binary_numbers) > 1:
        binary_numbers = get_rating(binary_numbers, idx + 1, oxygen=oxygen)

    return binary_numbers


if __name__ == '__main__':
    path = 'inputs.txt'
    binary_numbers = load_data(path)

    power_consumption = get_power_consumption(binary_numbers)
    print(f'Part 1 result: {power_consumption}')

    binary_numbers_copy = copy.deepcopy(binary_numbers)
    oxygen_rating = int(get_rating(binary_numbers, 0)[0], 2)
    co2_rating = int(get_rating(binary_numbers_copy, 0, oxygen=False)[0], 2)
    print(f'Part 2 result: {co2_rating*oxygen_rating}')