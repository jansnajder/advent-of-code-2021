# AoC 2021 - day 11
# Input file show paths between nodes.
#
# Part 1:  - Find how many routes are between start and end, if nodes in lowercase can be visited only once.
# Part 2:  - Nodes in lowercase can be visited twice! How many routes are there?

from typing import Dict, List


def load_data(path: str) -> Dict[str, List[str]]:
    '''
    Load data from file on input path. Data are represented as dict of possible paths from each node.

    :param path: path to input txt file
    :return nodes: dict of paths from each node
    '''
    nodes: Dict[str, List[str]] = {}

    with open(path, 'r', encoding='utf-8') as f:
        connections_raw = f.read().split('\n')

    for connection_raw in connections_raw:
        connection = connection_raw.split('-')

        if len(connection) == 2:
            paths: Dict[str, str] = {}
            paths[connection[0]] = connection[1]
            paths[connection[1]] = connection[0]

            for key, value in paths.items():
                if key in nodes:
                    nodes[key].append(value)
                else:
                    nodes[key] = [value]

    return nodes


def find_route_dfs(
    nodes: Dict[str, List[str]], opened: List[List[str]], routes: List[List[str]], visited_small_twice: bool
) -> List[List[str]]:
    '''
    Find route with help of depth first search.

    :param nodes: dict of connections
    :param opened: list of opened paths
    :param routes: list of routes from 'start' to 'end'
    :param visited_small_twice: bool indicating if nodes in lowercase can be visited twice
    :return routes: list of routes from 'start' to 'end'
    '''
    route = opened[0]
    node = route[-1]
    visited = []
    del opened[0]

    for node_ in route:
        if node_.islower():
            visited.append(node_)

    for value in nodes[node]:
        if value == 'end':
            routes.append(route + [value])
        elif value not in visited:
            opened.append(route + [value])
            routes = find_route_dfs(nodes, opened, routes, visited_small_twice)
        elif value in visited and not visited_small_twice:
            if value != 'start' and value != 'end':
                opened.append(route + [value])
                routes = find_route_dfs(nodes, opened, routes, True)

    return routes


if __name__ == '__main__':
    path = 'day_12/inputs.txt'
    nodes = load_data(path)
    route = ['start']
    routes: List[List[str]] = []

    opened = [route]
    routes = find_route_dfs(nodes, opened, routes, True)
    print(f'Result of part one: {len(routes)}')

    opened = [route]
    routes.clear()
    routes = find_route_dfs(nodes, opened, routes, False)
    print(f'Result of part two: {len(routes)}')
