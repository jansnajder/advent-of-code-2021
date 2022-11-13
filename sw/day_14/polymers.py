def load_data(path, polymer):
    with open(path, 'r', encoding='utf-8') as f:
        data_raw = f.read().split('\n')

    rules = {}
    polymer_dict = {}
    for line in data_raw:
        rules[line.split(' -> ')[0]] = line.split(' -> ')[1]

    for idx in range(len(polymer) - 1):
        if polymer[idx:idx + 2] in polymer_dict:
            polymer_dict[polymer[idx:idx + 2]] += 1
        else:
            polymer_dict[polymer[idx:idx + 2]] = 1

    return polymer_dict, rules


def polymerize(polymer_dict, rules, epochs):
    for epoch in range(epochs):
        new_polymer_dict = {}
        for key, val in polymer_dict.items():
            new_key_1 = key[0] + rules[key]
            new_key_2 = rules[key] + key[1]
            if new_key_1 in new_polymer_dict:
                new_polymer_dict[new_key_1] += val
            else:
                new_polymer_dict[new_key_1] = val
            if new_key_2 in new_polymer_dict:
                new_polymer_dict[new_key_2] += val
            else:
                new_polymer_dict[new_key_2] = val

        polymer_dict = new_polymer_dict

    return polymer_dict


def calculate_elements(polymer_dict):
    results = {}
    for key, val in polymer_dict.items():
        if key[0] in results:
            results[key[0]] += val
        else:
            results[key[0]] = val

    return results


if __name__ == '__main__':
    test_path = 'test_inputs.txt'
    test_polymer = 'NNCB'
    test_dict, test_rules = load_data(test_path, test_polymer)
    test_dict = polymerize(test_dict, test_rules, 40)
    results = calculate_elements(test_dict)
    print((max(list(results.values()))) - (min(list(results.values()))))

    path = 'inputs.txt'
    polymer = 'OOBFPNOPBHKCCVHOBCSO'
    polymer_dict, rules = load_data(path, polymer)
    polymer_dict = polymerize(polymer_dict, rules, 40)
    results = calculate_elements(polymer_dict)
    results[polymer[-1]] += 1
    print((max(list(results.values()))) - (min(list(results.values()))))
