# import math

# def floyd_warshall(graph):
#     v = len(graph)
    
#     dist = [row[:] for row in graph]
#     # dist =[]
#     # for row in graph:
#     #     dist.append(row[:])
    
#     for k in range(v):
#         for i in range(v):
#             for j in range(v):
#                 if dist[i][k] + dist[k][j] < dist[i][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]
#     return dist

# INF = math.inf
# graph = [
#     [0,   3,   INF, 7],
#     [8,   0,   2,   INF],
#     [5,   INF, 0,   1],
#     [2,   INF, INF, 0]
# ]

# dist = floyd_warshall(graph)

# print(dist)

# print("All pairs shortest paths:")
# for row in dist:
#     print(row)


import math
def floyd_warshall(graph):
    v = len(graph)
    
    dist = [row[:] for row in graph]
    
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

INF = math.inf
graph = [
    [0,   3,   INF, 7],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1],
    [2,   INF, INF, 0]
]

dist = floyd_warshall(graph)

print(dist)

print("All pairs shortest paths:")
for row in dist:
    print(row)