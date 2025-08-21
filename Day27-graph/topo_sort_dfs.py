class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
            
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
    
    def topological_sort_util(self, node, visited, stack):
        visited.add(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)
                
        stack.append(node)
    
    def topological_sort(self):
        visited = set()
        stack = []
        
        for node in self.graph:
            if node not in visited:
                self.topological_sort_util(node, visited, stack)
            
        return stack[::-1]

g = Graph()
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")

print(g.graph)
print("Topological Sort:", g.topological_sort())