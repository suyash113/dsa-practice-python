import heapq
from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    
    def dijkstra_path(self, start, goal):
        dist = {node:float('inf') for node in self.graph}
        dist[start] = 0
        pq = [(0, start)]
        parent = {start:None}
        # visited = set()
        # visited.add(start)
        while pq:
            curr_dist, node = heapq.heappop(pq)
            if node == goal:
                break
            for neighbor, weight in self.graph[node]:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    # if neighbor not in visited:
                    #     visited.add(neighbor)
                    parent[neighbor] = node
                    heapq.heappush(pq, (new_dist, neighbor))
        path = []
        # if goal in pq:
        curr = goal
        while curr:
            path.append(curr)
            curr = parent[curr]
        path.reverse()

        return path

g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("C", "B", 1)
g.add_edge("B", "D", 5)
g.add_edge("C", "D", 3)

print(g.graph)
print("Shortest path from A to D: ")
print(g.dijkstra_path("A", "D"))
