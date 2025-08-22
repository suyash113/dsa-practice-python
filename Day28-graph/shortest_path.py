# from collections import defaultdict, deque
# class Graph:
#     def __init__(self) -> None:
#         self.graph = defaultdict(list)
    
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
    
#     def bfs_shortest_path(self, start, goal):
#         visited = set()
#         parent = {start:None}
#         queue = deque([start])
#         visited.add(start)
#         while queue:
#             node = queue.popleft()
            
#             if node == goal:
#                 break
                
#             for neighbor in self.graph[node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     parent[neighbor] = node
#                     queue.append(neighbor)
#         # print(parent)
#         path = []
#         if goal in parent:
#             curr = goal
#             while curr:
#                 path.append(curr)
#                 curr = parent[curr]
#             path.reverse()
#         return path

# g= Graph()
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("B", "D")
# g.add_edge("C", "E")
# g.add_edge("D", "F")
# g.add_edge("E", "F")

# print(g.graph)
# print(g.bfs_shortest_path("A", "F"))

# from collections import defaultdict, deque
# class Graph:
#     def __init__(self) -> None:
#         self.graph = defaultdict(list)
    
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
    
#     def bfs_shortest_path(self, start, goal):
#         visited = set()
#         parent = {start:None}
#         queue = deque([start])
#         visited.add(start)
#         while queue:
#             node = queue.popleft()

#             if goal == node:
#                 break

#             for neighbor in self.graph[node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     parent[neighbor] = node
#                     queue.append(neighbor)
        
#         path = []
#         if goal in parent:
#             curr = goal
#             while curr:
#                 path.append(curr)
#                 curr = parent[curr]
#             path.reverse()
#         return path

# g= Graph()
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("B", "D")
# g.add_edge("C", "E")
# g.add_edge("D", "F")
# g.add_edge("E", "F")

# print(g.graph)
# print(g.bfs_shortest_path("A", "F"))


from collections import defaultdict, deque
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_shortest_path(self, start, goal):
        visited = set()
        parent = {start:None}
        visited.add(start)

        queue = deque([start])
        while queue:
            node = queue.popleft()
            
            if node == goal:
                break
                
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
            
        path = []
        if goal in parent:
            curr = goal
            while curr:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
        return path

g= Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")

print(g.graph)
print(g.bfs_shortest_path("A", "F"))