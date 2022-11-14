# AoC 2021 - day 3
# Input file shows seven segments number - each segment is one letter.
#
# Part 1:  - decode segment with known length and count how many of
#            them are in the input after |
# Part 2:  - decode all segments and sum all numbers after |

from typing import List, Tuple


def load_data(path: str) -> Tuple[List[List[str]], List[List[str]]]:
    '''
    Load seven segments data

    :param path: path to txt file
    :return first_part: part before |
    :return second_part: part after |
    '''
    with open(path, 'r', encoding='utf-8') as f:
        lines_raw = f.read().split('\n')

    first_part = []
    second_part = []

    for line in lines_raw:
        if ' | ' in line:
            first_part.append(line.split(' | ')[0].split(' '))
            second_part.append(line.split(' | ')[1].split(' '))

    return first_part, second_part


def count_known_output(segments: List[List[str]]) -> int:
    '''
    Count number of known numbers in second part of input.

    :param segments: segments definition
    :return count: number of known numbers, i.e., 1, 4, 7, 8
    '''
    lengths = [2, 3, 4, 7]  # length of known segments
    count = 0

    for output in segments:
        for segment in output:
            if len(segment) in lengths:
                count += 1

    return count


class SevenSegments():
    '''
    Class representing decoded seven segments

    :params first_part: segments before |
    :params second_part: segments after |
    '''

    def __init__(self, first_part: List[str], second_part: List[str]):
        # known numbers
        first_part = self.get_known_number(first_part)

        # unknown numbers
        self.get_unknown_number(first_part)

        self.numbers = [
            self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine
        ]

        #
        self.get_numbers_from_output(second_part)

    def get_known_number(self, segments: List[str]) -> List[str]:
        '''
        Decode numbers with known length, i.e, 1, 4, 7, 8

        :param segments: encoded segments
        :return segments_left: rest of encoded segments
        '''
        known_nums = {}
        known_lens = (0, 2, 0, 0, 4, 0, 0, 3, 7, 0)
        segments_left = []

        for segment in segments:
            if len(segment) in known_lens:
                known_nums[len(segment)] = sorted([letter for letter in segment])
            else:
                segments_left.append(segment)

        self.one = known_nums[2]
        self.seven = known_nums[3]
        self.four = known_nums[4]
        self.eight = known_nums[7]

        return segments_left

    def get_unknown_number(self, segments: List[str]) -> None:
        '''
        Decode numbers, which are not unique in length.

        Step by step:
            First part  - if all segments are in 4 and 1 -> it has to be 9
                        - if all segments are in only 1 -> it is either 3 or 0, depends on length

            Second part - from remaining only 6 has six segments
                        - 5 and 2 left -> 5 is subset of nine

        :param segments: unknown segments
        '''
        segment_left = []

        for segment in segments:
            if all(part in segment for part in self.four) and all(part in segment for part in self.one):
                self.nine = sorted([letter for letter in segment])
            elif all(part in segment for part in self.one):
                if len(segment) == 5:
                    self.three = sorted([letter for letter in segment])
                elif len(segment) == 6:
                    self.zero = sorted([letter for letter in segment])
            else:
                segment_left.append(segment)

        segments = segment_left

        for segment in segments:
            if len(segment) == 6:
                self.six = sorted([letter for letter in segment])
            else:
                if all(part in self.nine for part in segment):
                    self.five = sorted([letter for letter in segment])
                else:
                    self.two = sorted([letter for letter in segment])

    def get_numbers_from_output(self, segments):
        '''
        Calculate one number from second part of segments - e.g. 8, 9, 0 -> 890

        :param segments: encoded segments
        '''
        self.number = 0

        for segment in segments:
            segment_chars = sorted([letter for letter in segment])
            self.number = self.number * 10
            self.number += self.numbers.index(segment_chars)


if __name__ == '__main__':
    path = 'day_08/inputs.txt'
    first_part, second_part = load_data(path)

    print(f'Result of part one: {count_known_output(second_part)}.')

    segment = []

    for idx, _ in enumerate(first_part):
        segment.append(SevenSegments(first_part[idx], second_part[idx]))

    result = 0

    for output in segment:
        result += output.number

    print(f'Result of part two: {result}')
