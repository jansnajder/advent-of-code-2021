def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data_raw = f.read().split('\n')

    cubes = []
    for line in data_raw:
        if line.startswith('on '):
            on = True
            line = line.lstrip('on ')
        else:
            on = False
            line = line.lstrip('off ')

        axis = line.split(',')
        start = []
        end = []
        for coordinates in axis:
            coordinates = coordinates[2:]
            coordinate = list(map(int, coordinates.split('..')))
            start.append(coordinate[0])
            end.append(coordinate[1] + 1)

        start = tuple(start)
        end = tuple(end)
        cubes.append(Cube(on, start, end))

    return cubes


class Cube:

    def __init__(self, on, start, end):
        self.on = on
        self.start = start
        self.end = end

    def surrounds(self, other):
        return (
            self.start[0] <= other.start[0] <= other.end[0] <= self.end[0]
            and self.start[1] <= other.start[1] <= other.end[1] <= self.end[1]
            and self.start[2] <= other.start[2] <= other.end[2] <= self.end[2]
        )

    def intersects(self, other):
        return (
            self.start[0] < other.end[0] and other.start[0] < self.end[0] and self.start[1] < other.end[1]
            and other.start[1] < self.end[1] and self.start[2] < other.end[2] and other.start[2] < self.end[2]
        )


class Cubeoid:

    def __init__(self):
        self.cubes = []

    def __str__(self):
        total = 0
        for cube in self.cubes:
            total += (cube.end[0] - cube.start[0]) * (cube.end[1] - cube.start[1]) * (cube.end[2] - cube.start[2])
        return (f'Total cubes turned on: {total}')

    def add(self, cube_to_add):
        new_cubes = []
        to_remake = []
        # get to know relation of new cube to current cubes
        for cube in self.cubes:
            if cube.surrounds(cube_to_add):
                return
            elif cube_to_add.surrounds(cube):
                continue
            elif not cube.intersects(cube_to_add):
                new_cubes.append(cube)
            else:
                to_remake.append(cube)

        to_remake.append(cube_to_add)
        for cube_candidate in self.new_cube_candidates(to_remake):
            for cube in to_remake:
                if cube.intersects(cube_candidate):
                    new_cubes.append(cube_candidate)
                    break

        self.cubes = new_cubes

    def new_cube_candidates(self, to_remake):
        # AABB stackoverflow https://stackoverflow.com/questions/66135217/
        # how-to-subdivide-set-of-overlapping-aabb-into-non-overlapping-set-of-aabbs
        xs = set()
        ys = set()
        zs = set()
        for cube in to_remake:
            xs.add(cube.start[0])
            xs.add(cube.end[0])
            ys.add(cube.start[1])
            ys.add(cube.end[1])
            zs.add(cube.start[2])
            zs.add(cube.end[2])

        x_boundaries = sorted(xs)
        y_boundaries = sorted(ys)
        z_boundaries = sorted(zs)

        for x_start, x_end in zip(x_boundaries, x_boundaries[1:]):
            for y_start, y_end in zip(y_boundaries, y_boundaries[1:]):
                for z_start, z_end in zip(z_boundaries, z_boundaries[1:]):
                    start = [x_start, y_start, z_start]
                    end = [x_end, y_end, z_end]
                    yield Cube(True, start, end)

    def subtract(self, cube_to_add):
        new_cubes = []
        to_remake = []
        for cube in self.cubes:
            if cube_to_add.surrounds(cube):
                continue
            elif not cube.intersects(cube_to_add):
                new_cubes.append(cube)
            else:
                to_remake.append(cube)

        to_remake.append(cube_to_add)
        for cube_candidate in self.new_cube_candidates(to_remake):
            if cube_candidate.intersects(cube_to_add):
                continue
            for cube in to_remake:
                if cube_candidate.intersects(cube):
                    new_cubes.append(cube_candidate)
                    break

        self.cubes = new_cubes


if __name__ == '__main__':
    path = 'input.txt'
    cubes = load_data(path)
    cubeoid = Cubeoid()
    i = 1
    for cube in cubes:
        if cube.on:
            cubeoid.add(cube)
        else:
            cubeoid.subtract(cube)
        print(i)
        i += 1

    print(cubeoid)
