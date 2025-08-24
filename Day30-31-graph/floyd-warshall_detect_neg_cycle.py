INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    
    dist = [[INF] * n for _ in graph]
    
    for u in range(n):
        for v in range(n):
            dist[u][v] = graph[u][v]
        
    for i in range(v):
        dist[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                
    negative_cycle = False
    for i in range(n):
        if dist[i][i] < 0:
            negative_cycle = True
            print(f"Negative cycle detected at vertex {i}")
    return dist, negative_cycle


graph = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

dist, cycle = floyd_warshall(graph)

print("\nAll-Pairs Shortest Path Matrix:")
for row in dist:
    print(row)

if not cycle:
    print("\nNo negative cycle detected.")
