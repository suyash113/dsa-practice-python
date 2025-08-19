from collections import defaultdict
class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def remove_edge(self, u,v):
        if v in self.graph[u]:
            self.graph[u].remove(v)
        if u in self.graph[v]:
            self.graph[v].remove(u)
    
    def remove_vertex   (self, v):
        if v in self.graph:
            for neighbor in list(self.graph[v]):
                self.graph[neighbor].remove(v)
            del self.graph[v]
            
    
    def print_list(self):
        print("Adjacency List: ")
        for node in self.graph:
            print(node, "->", self.graph[node])
        
g = GraphList()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")

print("Original:")
g.print_list()

print("\nAfter removing edge A-B:")
g.remove_edge("A", "B")
g.print_list()

print("\nAfter removing vertex C:")
g.remove_vertex("C")
g.print_list()