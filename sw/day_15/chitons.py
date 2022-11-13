import numpy as np
import heapq


def load_data(path):
    chiton_map = np.genfromtxt(path, dtype=int, delimiter=1)
    height, width = chiton_map.shape
    return chiton_map, height, width


def dijkstra(chiton_map, height, width, scale):
    distances = {(0, 0): 0}
    opened = [(0, (0, 0))]
    while len(opened) > 0:
        total, (x, y) = heapq.heappop(opened)
        if total <= distances[(x, y)]:
            for n in neighbours(x, y, width, height, scale):
                distance = total + cost(*n, chiton_map, height, width)
                if distance < distances.get(n, 1e308):
                    distances[n] = distance
                    heapq.heappush(opened, (distance, n))

    return distances[(width * scale - 1, height * scale - 1)]


def neighbours(x, y, width, height, scale):
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in out if 0 <= a < width * scale and 0 <= b < height * scale]


def cost(x, y, chiton_map, height, width):
    c = chiton_map[y % height][x % width]
    c = (c + x // width + y // height)
    c = 1 + (c - 1) % 9
    return c


if __name__ == '__main__':
    path = 'inputs.txt'
    chiton_map, height, width = load_data(path)
    print(dijkstra(chiton_map, height, width, 5))  # 2817
