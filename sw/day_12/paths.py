def load_data(path):
    nodes = {}

    with open(path, 'r', encoding='utf-8') as f:
        connections_raw = f.read().split('\n')

    for connection_raw in connections_raw:
        connection = connection_raw.split('-')

        if len(connection) == 2:
            paths = {}
            paths[connection[0]] = connection[1]
            paths[connection[1]] = connection[0]

            for key, value in paths.items():
                if key in nodes:
                    nodes[key].append(value)
                else:
                    nodes[key] = [value]

    return nodes


def find_route_dfs(nodes, opened, routes, visited_small_twice):
    route = opened[0]
    node = route[-1]
    visited = []
    del opened[0]

    for node in route:
        if node.islower():
            visited.append(node)

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
    opened = [route]
    routes = []
    routes = find_route_dfs(nodes, opened, routes, False)
    print(len(routes))
