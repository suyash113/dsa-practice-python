from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def topo_sort_kahns(self):
        indegree = defaultdict(int)
        
        for node in self.graph:
            for neighbor in self.graph[node]:
                indegree[neighbor] += 1
                
        for node in self.graph:
            if node not in indegree:
                indegree[node] = 0
            
        
        queue = deque([node for node in indegree if indegree[node] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in self.graph[node]:
                indegree[neighbor] -= 1     
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                
        if len(topo_order) != len(indegree):
            return "Cycle detected → Topological Sort not possible"
        
        return topo_order

g = Graph()
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")

print(g.graph)
print("Kahn's Topological Sort:", g.topo_sort_kahns())