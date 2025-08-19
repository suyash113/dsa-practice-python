class GraphMatrix:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0]* vertices for _ in range(vertices)]
        
    def add_edge(self, u, v):
        # for undirected edges
        
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    
    def remove_edge(self, u,v):
        self.graph[u][v] = 0
        self.graph[v][u] = 0
    
    def remove_vertex(self,v):
        self.graph.pop(v)
        for row in self.graph:
            row.pop(v)
        self.v -= 1
        
    def print_matrix(self):
        print("Adjacency graph: ")
        for row in self.graph:
            print(row)
    
g = GraphMatrix(3)
g.add_edge(0, 1)  # A-B
g.add_edge(0, 2)  # A-C
g.add_edge(1, 2)  # B-C

print("Original:")
g.print_matrix()

print("\nAfter removing edge A-B:")
g.remove_edge(0, 1)
g.print_matrix()

print("\nAfter removing vertex C:")
g.remove_vertex(2)
g.print_matrix()