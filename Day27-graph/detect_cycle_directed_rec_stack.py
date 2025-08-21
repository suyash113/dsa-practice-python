# from collections import defaultdict
# class Graph:
#     def __init__(self) -> None:
#         self.graph = {}

#     def add_edge(self, u, v):
#         if u not in self.graph:
#             self.graph[u] = []
#         if v not in self.graph:
#             self.graph[v] = []
#         self.graph[u].append(v)
    
#     def is_cyclic_util(self, node, visited, rec_stack):
#         visited.add(node)
#         rec_stack.add(node)

#         for neighbor in self.graph[node]:
#             if neighbor not in visited:
#                 if self.is_cyclic_util(neighbor, visited, rec_stack):
#                     return True
#             elif neighbor in rec_stack:
#                 return True
#         rec_stack.remove(node)
#         return False
    
#     def is_cyclic(self):
#         visited = set()
#         rec_stack = set()

#         for node in self.graph.keys():
#             if node not in visited:
#                 if self.is_cyclic_util(node, visited, rec_stack):
#                     return True        
#         return False
        
# g = Graph()
# g.add_edge("A", "B")
# g.add_edge("B", "C")
# g.add_edge("C", "D")
# print(g.graph)
# print("Graph is cyclic? ", g.is_cyclic())





class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def is_cyclic_util(self, node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(node)
        return False
    
    def is_cyclic(self):
        visited = set()
        rec_stack = set()
    
        for node in self.graph:
            if node not in visited:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

g = Graph()
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "A")
print(g.graph)
print("Graph is cyclic? ", g.is_cyclic())