from typing import List, Tuple


def load_data(path: str) -> Tuple[List[str], List[str]]:
    with open(path, 'r', encoding='utf-8') as f:
        lines_raw = f.read().split('\n')

    first_part = []
    second_part = []
    for line in lines_raw:
        first_part.append(line.split(' | ')[0].split(' '))
        second_part.append(line.split(' | ')[1].split(' '))

    return first_part, second_part


def count_known_output(segments):
    lengths = [2, 3, 4, 7]  # length of known segments

    count = 0
    for output in segments:
        for segment in output:
            if len(segment) in lengths:
                count += 1

    return count


# rules:
# vím že dva pravé segmenty jsou jednička
# segment pro sedmičku minus segment pro jedničku mi dá horní
# segment pro čtyřku minus segment pro jedničku mi da prostředek a levy horni
# segment s délkou šest, který obsahuje pět segmentů, které už jsou detekované je devítka -> dostanu spodní
# segment s délkou šest, ten druhý, je šestka - dostanu levý spodní a pravý horní
# jsem schopný zjistit co je dvojka a pětka a trojka

#  000
# 1   2
# 1   2
#  333
# 4   4
# 4   5
#  666


class SevenSegments():

    def __init__(self, first_part, second_part):

        self.zero = []
        self.one = []
        self.two = []
        self.three = []
        self.four = []
        self.five = []
        self.six = []
        self.seven = []
        self.eight = []
        self.nine = []

        # known numbers
        self.get_known_number(first_part)

        # unknown numbers
        self.get_unknown_number(first_part)

        self.numbers = [
            self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine
        ]

        #
        self.get_numbers_from_output(second_part)

    def get_known_number(self, segments):
        for segment in segments:
            if len(segment) == 2:
                for letter in segment:
                    self.one.append(letter)
                self.one = sorted(self.one)
            if len(segment) == 3:
                for letter in segment:
                    self.seven.append(letter)
                self.seven = sorted(self.seven)
            if len(segment) == 4:
                for letter in segment:
                    self.four.append(letter)
                self.four = sorted(self.four)
            if len(segment) == 7:
                for letter in segment:
                    self.eight.append(letter)
                self.eight = sorted(self.eight)

    def get_unknown_number(self, segments):
        for segment in segments:
            if len(segment) == 6:
                if all(part in segment for part in self.four) and all(part in segment for part in self.one):
                    for letter in segment:
                        self.nine.append(letter)
                    self.nine = sorted(self.nine)
            if len(segment) == 5:
                if all(part in segment for part in self.one):
                    for letter in segment:
                        self.three.append(letter)
                    self.three = sorted(self.three)

        for segment in segments:
            if len(segment) == 6:
                if all(part in segment for part in self.seven) and not all(part in segment for part in self.nine):
                    for letter in segment:
                        self.zero.append(letter)
                    self.zero = sorted(self.zero)

        for segment in segments:
            if len(segment) == 6:
                if not all(part in segment for part in self.zero) and not all(part in segment for part in self.nine):
                    for letter in segment:
                        self.six.append(letter)
                    self.six = sorted(self.six)

        for segment in segments:
            if len(segment) == 5:
                if all(part in self.six for part in segment):
                    for letter in segment:
                        self.five.append(letter)
                    self.five = sorted(self.five)

        for segment in segments:
            if len(segment) == 5:
                if not all(part in segment for part in self.five) and not all(part in segment for part in self.three):
                    for letter in segment:
                        self.two.append(letter)
                    self.two = sorted(self.two)

    def get_numbers_from_output(self, output):
        segment_list = []
        for idx, segment in enumerate(output):
            segment_list.append([])
            for letter in segment:
                segment_list[idx].append(letter)
            segment_list[idx] = sorted(segment_list[idx])

        self.number = 0
        for idx, segment in enumerate(segment_list):
            self.number = self.number * 10
            self.number += self.numbers.index(segment)


if __name__ == '__main__':
    path = 'day_08/inputs.txt'
    first_part, second_part = load_data(path)

    count = count_known_output(second_part)
    print(count)

    segment = []

    for idx, _ in enumerate(first_part):
        segment.append(SevenSegments(first_part[idx], second_part[idx]))

    result = 0

    for output in segment:
        result += output.number

    print(result)
