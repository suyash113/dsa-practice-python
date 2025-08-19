# from collections import defaultdict, deque
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
    
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
    
#     def print_list(self):
#         print("Adjacency List: ")
#         for node in self.graph:
#             print(node, "->", self.graph[node])
    
#     def bfs(self, start):
#         visited = set()
#         queue = deque([start])

#         print("BFS Traversal: \n")
#         while queue:
#             node = queue.popleft()
#             if node not in visited:
#                 print(node, end=" ")
#                 visited.add(node)
            
#             for neighbor in self.graph:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#         print()
    
# g = Graph()
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("B", "D")
# g.add_edge("C", "E")
# g.add_edge("D", "E")
# g.add_edge("E", "F")

# g.bfs("A")












from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def print_list(self):
        print("Adjacency List: ")
        for node in self.graph:
            print(node, "->", self.graph[node])
        
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        print("BFS Traversal: \n")
        
        while queue:
            node = queue.popleft()
            
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()
        

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("E", "F")

g.print_list()
g.bfs("A")