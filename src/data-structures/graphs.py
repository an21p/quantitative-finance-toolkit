def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        visited.add(current)
        print(current)
        for adj in graph[current]:
            if adj not in visited and adj not in stack:
                stack.append(adj)
        print(stack)


def bfs(graph, start):
    queue = [start]
    visited = set()

    while queue:
        current = queue.pop()
        visited.add(current)
        print(current)
        for adj in graph[current]:
            if adj not in visited and adj not in queue:
                queue.insert(0,adj)
        print(queue)


if __name__ == "__main__":
    g = {'0': ['1', '2'],
             '1': ['0', '3', '4'],
             '2': ['0', '5'],
             '3': ['1'],
             '4': ['1'],
             '5': ['2']}

    dfs(g, '0')
    print()
    bfs(g, '0')
