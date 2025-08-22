class Graph:
    def __init__(self):
        self.edge = []
        self.v = set()
    
    def add_edge(self, u,v,w):
        self.edge.append((u,v,w))
        self.v.add(u)
        self.v.add(v)
    
    def bellman_ford(self, start):
        dist = {i:float('inf') for i in self.v}
        dist[start] = 0
        
        for _ in range(len(self.v)-1):
            for u,v,w in self.edge:
                if dist[u] + w < dist[v] and dist[u] != float('inf'):
                    dist[v] = dist[u] + w
                
        for i in range(len(self.v)):
            if dist[u] + w < dist[v] and dist[v] != float('inf'):
                print("Negative cycle detected ")
        
        return dist

g = Graph()
g.add_edge("S", "E", 8)
g.add_edge("S", "A", 10)
g.add_edge("E", "D", 1)
g.add_edge("D", "A", -4)
g.add_edge("D", "C", -1)
g.add_edge("A", "B", 1)
g.add_edge("C", "B", -2)
g.add_edge("C", "A", 2)

print("Shortest distances from S:")
print(g.bellman_ford("S"))
