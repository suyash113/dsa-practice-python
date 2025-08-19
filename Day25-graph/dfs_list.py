# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
    
#     def add_edge(self, u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
    
#     def print_graph(self):
#         print("Adjacency List: ")
#         for node in self.graph:
#             print(node, "->", self.graph[node])
        
#     def dfs(self, start):
#         visited = set()
        
#         def dfs_recursive(node):
#             if node not in visited:
#                 print(node, end=" ")
#                 visited.add(node)
#                 for neighbor in self.graph[node]:
#                     dfs_recursive(neighbor)
                
#         print("DFS Traversal:", end=" ")
#         dfs_recursive(start)
#         print()

        

# g = Graph()
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("B", "D")
# g.add_edge("C", "E")
# g.add_edge("D", "E")
# g.add_edge("E", "F")

# g.print_graph()
# g.dfs("A")









from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def print_graph(self):
        print("Adjacency List: ")
        for node in self.graph:
            print(node, "->", self.graph[node])
    
    def dfs(self, start):
        visited = set()
        
        def dfs_recursive(node):
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph[node]:
                    dfs_recursive(neighbor)
                
        print("DFS Traversal: " , end=" ")
        dfs_recursive(start)
        print()
    
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("E", "F")

g.print_graph()
g.dfs("A")
