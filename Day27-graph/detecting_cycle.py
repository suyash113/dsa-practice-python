# from collections import defaultdict, deque
# class Graph:
#     def __init__(self) -> None:
#         self.graph = defaultdict(list)
    
#     def add_edge(self, u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)

#     def detect_cycle(self, node, visited, parent):
#         visited.add(node)

#         for neighbor in self.graph[node]:
#             if neighbor not in visited:
#                 if self.detect_cycle(neighbor, visited, node):
#                     return True
#             elif parent and neighbor != parent:
#                 return True
#         return False
    
#     def is_cyclic(self):
#         visited = set()
#         for node in self.graph:
#             if node not in visited:
#                 if self.detect_cycle(node, visited, None):
#                     return True
#         return False
    
# g = Graph()
# g.add_edge("A", "B")
# g.add_edge("B", "C")
# g.add_edge("C", "D")
# print(g.graph)
# print("Graph is cyclic? ", g.is_cyclic())






from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, node, visited, parent):
        visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.is_cyclic_util(neighbor, visited, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    def is_cyclic(self):
        visited = set()

        for node in self.graph:
            if node not in visited:
                if self.is_cyclic_util(node, visited, None):
                    return True
        return False
    
g = Graph()
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "A")
print(g.graph)
print("Graph is cyclic? ", g.is_cyclic())
