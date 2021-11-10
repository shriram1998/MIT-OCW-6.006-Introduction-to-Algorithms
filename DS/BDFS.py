import collections
from typing import List


def bfs(graph, s):
    visited = [s]
    queue = collections.deque([s])
    parent = {s: None}
    level = {s: 0}
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            print(vertex)
            if neighbour not in visited:
                # print('Visited', neighbour)
                parent[neighbour] = vertex
                level[neighbour] = level[vertex]+1
                visited.append(neighbour)
                queue.append(neighbour)
    print(parent, level)


def dfs_visit(graph: object, key: str, visited: List, iter: int):
    print(iter, key)
    for neighbour in graph[key]:
        if neighbour not in visited:
            visited.append(neighbour)
            dfs_visit(graph, neighbour, visited, iter)


def dfs(graph):
    iter = 0
    visited = []
    for key, val in graph.items():
        visited.append(key)
        dfs_visit(graph, key, visited, iter)
        iter += 1
        visited = []


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set(['A'])}
dfs(graph)
