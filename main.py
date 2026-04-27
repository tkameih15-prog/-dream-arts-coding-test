import sys
from collections import defaultdict

def parse_input():
    graph = defaultdict(list)
    nodes = set()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")

        if len(parts) != 3:
            continue

        u = int(parts[0].strip())
        v = int(parts[1].strip())
        w = float(parts[2].strip())

        graph[u].append((v, w))
        graph[v].append((u, w))

        nodes.add(u)
        nodes.add(v)

    return graph, nodes


def find_longest_path(graph, nodes):
    best_distance = -1
    best_path = []

    def dfs(current, visited, distance, path):
        nonlocal best_distance, best_path

        if distance > best_distance:
            best_distance = distance
            best_path = path[:]

        for nxt, w in graph[current]:
            if nxt not in visited:
                visited.add(nxt)
                path.append(nxt)

                dfs(nxt, visited, distance + w, path)

                path.pop()
                visited.remove(nxt)

    for start in nodes:
        dfs(start, {start}, 0, [start])

    return best_path


def main():
    graph, nodes = parse_input()

    if not nodes:
        return

    path = find_longest_path(graph, nodes)

    for node in path:
        print(node)


if __name__ == "__main__":
    main()
