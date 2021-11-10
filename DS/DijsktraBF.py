import heapq
import sys
graph = [[0, sys.maxsize, 1, 2, sys.maxsize, sys.maxsize, sys.maxsize],
         [sys.maxsize, 0, 2, sys.maxsize, sys.maxsize, 3, sys.maxsize],
         [-5, 2, 0, 1, 3, sys.maxsize, sys.maxsize],
         [2, sys.maxsize, 1, 0, sys.maxsize, sys.maxsize, 1],
         [sys.maxsize, sys.maxsize, 3, sys.maxsize, 0, 2, sys.maxsize],
         [sys.maxsize, 3, sys.maxsize, sys.maxsize, 2, 0, 1],
         [sys.maxsize, sys.maxsize, sys.maxsize, 1, sys.maxsize, 1, 0]]


def Dijkstra(graph, source):
    numOfVertices = len(graph[0])
    distance = []
    prev = []
    pq = []
    unvisited = []
    for _ in range(numOfVertices):
        distance.append(sys.maxsize)
        prev.append(None)
        unvisited.append(True)
    pq.append((0, source))
    distance[source] = 0
    unvisited[source] = False
    while(len(pq)):
        (targetVal, targetKey) = heapq.heappop(pq)
        unvisited[targetKey] = False
        row = graph[targetKey]
        for ix, vertex in enumerate(row):
            if row[ix] == sys.maxsize:
                continue
            tempDistance = targetVal+vertex
            if(tempDistance < distance[ix]):
                distance[ix] = tempDistance
                prev[ix] = targetKey
            if unvisited[ix]:
                heapq.heappush(pq, (distance[ix], ix))
    print(distance, prev)

# BellmanFord


def BF(graph, source):
    numOfVertices = len(graph[0])
    distance = []
    prev = []
    pq = []
    unvisited = []
    for _ in range(numOfVertices):
        distance.append(sys.maxsize)
        prev.append(None)
        unvisited.append(True)
    pq.append((0, source))
    distance[source] = 0
    for iv, vertex in enumerate(graph):
        for ie, edge in enumerate(vertex):
            tempDistance = distance[iv]+edge
            if(tempDistance < distance[ie]):
                distance[ie] = tempDistance
                prev[ie] = iv
    for iv, vertex in enumerate(graph):
        for ie, edge in enumerate(vertex):
            if(distance[iv]+edge < distance[ie]):
                print('Negative cycles exist')
    print(distance, prev)


Dijkstra(graph, 0)
