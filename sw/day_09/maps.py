# AoC 2021 - day 9
# Input file shows map of heights
#
# Part 1:  - find coordinates of local minimums, result is sum of heights of minimums + number of
#            minimums
# Part 2:  - find three largest basins (area of heights lower than 8), result is multiplication
#            of sizes

from typing import List, Tuple

TCoordinates = List[Tuple[int, int]]


def load_data(path: str) -> List[str]:
    '''
    Load data from input txt file

    :param path: path to input file
    :return height_map: list of strings representing heights
    '''
    with open(path, 'r', encoding='utf-8') as f:
        height_map = f.read().split('\n')

    return height_map


class HeightMap:
    '''
    Class encapsulating height map.

    :params height_map: list of strings representing height map
    '''

    def __init__(self, height_map: List[str]) -> None:
        self.height_map = height_map
        self.rows = len(height_map)
        self.cols = len(height_map[0])

    def _find_neighbors(self, coordinate: Tuple[int, int]) -> TCoordinates:
        '''
        Find coordinates of neighbors of given coordinates - 4 way.

        :param coordinate: x, y coordinates of point to find neighbors of
        :return neighbors: list of neighboring coordinates
        '''
        neighbors: TCoordinates = []

        if coordinate[0] > 0:
            neighbors.append((coordinate[0] - 1, coordinate[1]))
        if coordinate[1] > 0:
            neighbors.append((coordinate[0], coordinate[1] - 1))
        if coordinate[0] < (self.rows - 1):
            neighbors.append((coordinate[0] + 1, coordinate[1]))
        if coordinate[1] < (self.cols - 1):
            neighbors.append((coordinate[0], coordinate[1] + 1))

        return neighbors

    def _expand_coordinates(self, closed: TCoordinates, opened: TCoordinates,
                            size: int) -> Tuple[int, TCoordinates, TCoordinates]:
        '''
        Expand first coordinate of opened list. If the neighbor is not 9, add it to opened list. While there are coordinates on
        opened list, call expand_coordinates again.

        :param closed: list of already expanded coordinates
        :param opened: list of coordinates to expand
        :param size: current size of basin
        :return size: new size of basin
        :return closed: actualized closed list
        :return opened: actualized opened list
        '''
        coordinates = opened[0]
        del opened[0]
        size += 1
        neighbors = self._find_neighbors((coordinates[0], coordinates[1]))

        for neighbor in neighbors:
            if self.height_map[neighbor[0]][neighbor[1]] != '9':
                if neighbor not in (closed + opened):
                    opened.append(neighbor)

        closed.append(coordinates)

        if len(opened) > 0:
            size, closed, opened = self._expand_coordinates(closed, opened, size)

        return size, closed, opened

    def get_mins(self) -> TCoordinates:
        '''
        Find coordinates of local minimums.

        :return minimum_coordinates: list of coordinates of local minimums
        '''
        minimums_coordinates: TCoordinates = []

        for row_idx, row in enumerate(height_map):
            for height_idx, height in enumerate(row):
                for neighbor in self._find_neighbors((row_idx, height_idx)):
                    if int(height) >= int(self.height_map[neighbor[0]][neighbor[1]]):
                        break
                else:
                    minimums_coordinates.append((row_idx, height_idx))

        return minimums_coordinates

    def part_one(self) -> int:
        '''Method representing part one.'''
        mins_coordinates = self.get_mins()

        mins = 0

        for coordinate in mins_coordinates:
            mins += int(self.height_map[coordinate[0]][coordinate[1]])

        retval = mins + len(mins_coordinates)

        return retval

    def part_two(self) -> int:
        '''Method representing part two.'''
        mins_coordinates = self.get_mins()
        sizes: List[int] = []

        for coordinates in mins_coordinates:
            size = 0
            closed: TCoordinates = []
            opened: TCoordinates = [coordinates]
            size, _, _ = self._expand_coordinates(closed, opened, size)
            sizes.append(size)

        sizes.sort(reverse=True)
        result = 1

        for i in range(3):
            result *= sizes[i]

        return result


if __name__ == '__main__':
    path = 'day_09/inputs.txt'
    height_map = load_data(path)
    hm = HeightMap(height_map)
    print(f'Result of part 1 is: {hm.part_one()}')
    print(f'Result of part 2 is: {hm.part_two()}')
