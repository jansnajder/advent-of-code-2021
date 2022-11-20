# AoC 2021 - day 5
# Input file shows starting and ending positions of farm.
#
# Part 1:  - Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
# Part 2:  - Consider all of the lines, i.e, even diagonals. At how many points do at least two lines overlap?

from typing import List


class Farm:
    '''
    Representation of farm

    :param line: list of starting and ending farm coordinates
    '''

    def __init__(self, line: List[List[int]]):
        self.x1: int = line[0][0]
        self.y1: int = line[0][1]
        self.x2: int = line[1][0]
        self.y2: int = line[1][1]
        self.processed = False

    def update_matrix_regular(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        Update farm land matrix with vertical and horizontal farms position.

        :param matrix: farm land matrix
        :return matrix: update farm land matrix
        '''
        if self.x1 == self.x2:
            self.processed = True
            min_y = min([self.y1, self.y2])
            max_y = max([self.y1, self.y2])

            for i in range(min_y, max_y + 1):
                matrix[i][self.x1] += 1

        elif self.y1 == self.y2:
            self.processed = True
            min_x = min([self.x1, self.x2])
            max_x = max([self.x1, self.x2])

            for i in range(min_x, max_x + 1):
                matrix[self.y1][i] += 1

        return matrix

    def update_matrix_diagonal(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        Update farm land matrix with diagonal farms position.

        :param matrix: farm land matrix
        :return matrix: update farm land matrix
        '''
        if self.x1 < self.x2:
            if self.y1 < self.y2:
                y = self.y1

                for i in range(self.x1, self.x2 + 1):
                    matrix[y][i] += 1
                    y += 1
            else:
                y = self.y1

                for i in range(self.x1, self.x2 + 1):
                    matrix[y][i] += 1
                    y -= 1
        else:
            if self.y1 < self.y2:
                y = self.y1

                for i in range(self.x1, self.x2 - 1, -1):
                    matrix[y][i] += 1
                    y += 1
            else:
                y = self.y1

                for i in range(self.x1, self.x2 - 1, -1):
                    matrix[y][i] += 1
                    y -= 1

        self.processed = True
        return matrix


def load_data(path: str) -> List[List[List[int]]]:
    '''
    Load input data

    :param path: path to txt input file
    :return data: task inputs
    '''
    with open(path, 'r', encoding='utf-8') as f:
        lines: List[str] = f.read().split('\n')

    data: List[List[List[int]]] = []

    for line in lines:
        coordinates_raw = line.split(' -> ')
        coordinates: List[List[int]] = []

        for value in coordinates_raw:
            value = value.replace(' ', ',')
            coordinates.append(list(map(int, value.split(','))))

        data.append(coordinates)

    return data


def get_dangerous_area(farm_land: List[List[int]]) -> int:
    '''
    Sums number of farms where value is more than one.

    :param farm_land: matrix of farms
    :return dangerous_area: number of farms with value more than one
    '''
    dangerous_area = 0

    for farm_line in farm_land:
        for farm in farm_line:
            if farm > 1:
                dangerous_area += 1

    return dangerous_area


if __name__ == '__main__':
    path = 'day_05/inputs.txt'
    coordinates = load_data(path)
    farm_land = [[0 for col in range(1000)] for row in range(1000)]
    farms = [Farm(coordinate) for coordinate in coordinates]

    for farm in farms:
        farm_land = farm.update_matrix_regular(farm_land)

    print(f'Part 1 result: {get_dangerous_area(farm_land)}')

    for farm in farms:
        if not farm.processed:
            farm_land = farm.update_matrix_diagonal(farm_land)

    print(f'Part 2 result: {get_dangerous_area(farm_land)}')
