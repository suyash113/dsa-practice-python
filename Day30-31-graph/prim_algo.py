# import heapq
# from collections import defaultdict
# class Graph:
#     def __init__(self):
#          self.graph = defaultdict(list)
        
#     def add_edge(self, u, v, w):
#         self.graph[u].append((v, w))
#         self.graph[v].append((u,w))
    
#     def prim(self, start):
#         visited = set()
#         mst = []
#         min_heap = [(0,start,None)]
        
#         while min_heap:
#             weight ,node, parent = heapq.heappop(min_heap)
            
#             if node in visited:
#                 continue
#             visited.add(node)
            
#             if parent:
#                 mst.append((parent, node, weight))
            
#             for neighbor, w in self.graph[node]:
#                 if neighbor not in visited:
#                     heapq.heappush(min_heap, (w, neighbor,node))
                    
#         return mst
    
# g = Graph()
# g.add_edge("A", "B", 2)
# g.add_edge("A", "C", 3)
# g.add_edge("B", "C", 1)

# mst = g.prim("A")
# print("MST:", mst)




import heapq
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u,w))
        
    def prim(self, start):
        visited = set()
        mst = []
        min_heap = [(0, start, None)]
        
        while min_heap:
            weight, node, parent = heapq.heappop(min_heap)
            
            if node in visited:
                continue
            visited.add(node)
            
            if parent:
                mst.append((parent, node, weight))
                
            for neighbor, w in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor, node))
        
        return mst

g = Graph()
g.add_edge("A", "B", 2)
g.add_edge("A", "C", 3)
g.add_edge("B", "C", 1)

mst = g.prim("A")
print("MST:", mst)