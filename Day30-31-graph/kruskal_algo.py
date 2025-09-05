# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0]*n

#     def find(self, u):
#         prnt = self.parent[u]
#         if prnt != u:
#             self.parent[u] = self.find(self.parent[u])
#         return self.parent[u]
    
#     def union(self, u, v):
#         root_u = self.find(u)
#         root_v = self.find(v)
        
#         if root_u == root_v:
#             return False
        
#         a = self.rank[root_u]
#         b = self.rank[root_v]
#         if self.rank[root_u] < self.rank[root_v]:
#             self.parent[root_u] = root_v
#         elif self.rank[root_u] > self.rank[root_v]:
#             self.parent[root_v] = root_u
#         else:
#             self.parent[root_v] = root_u
#             self.rank[root_u] += 1
        
#         return True

# def kruskal(n, edges):
#     edges.sort()
#     uf = UnionFind(n)
#     mst = []
#     total_weight = 0
    
#     for weight, u, v in edges:
#         if uf.union(u,v):
#             mst.append((u, v, weight))
#             total_weight += weight
            
#     return mst, total_weight

# n = 5

# edges = [
#     (1,0,1),
#     (3,0,2),
#     (2,1,2),
#     (4,1,3),
#     (5,2,3),
#     (7,3,4),
#     (6,2,4)
# ]

# mst, total = kruskal(n, edges)
# print("Edges in mst: ", mst)
# print("Total weight:", total)


# class DisjointSet:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0]*n
    
#     def find(self, u):
#         if self.parent[u] != u:
#             self.parent[u] = self.find(self.parent[u])
#         return self.parent[u]

#     def union(self, u, v):
#         root_u = self.find(u)
#         root_v  = self.find(v)

#         if root_u == root_v:
#             return False

#         if self.rank[root_u] < self.rank[root_v]:
#             self.parent[root_u] = root_v
#         elif self.rank[root_u] > self.rank[root_v]:
#             self.parent[root_v] = root_u
#         else:
#             self.parent[root_u] = root_v
#             self.rank[root_u] += 1
        
#         return True
    
# def kruskal(n, edges):
#     edges.sort()
#     mst = []
#     ds = DisjointSet(n)
#     total_weight = 0

#     for w, u, v in edges:
#         if ds.union(u, v):
#             mst.append((u,v,w))
#             total_weight += w

#     return mst, total_weight


# n = 5

# edges = [
#     (1,0,1),
#     (3,0,2),
#     (2,1,2),
#     (4,1,3),
#     (5,2,3),
#     (7,3,4),
#     (6,2,4)
# ]

# mst, total = kruskal(n, edges)
# print("Edges in mst: ", mst)
# print("Total weight:", total)



class unionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v
            self.rank[root_u] += 1
        
        return True

def kruskal(n, edges):
    uf = unionFind(n)
    mst = []
    total_weight = 0

    for  w, u, v in edges:
        if uf.union(u, v):
            mst.append((u,v,w))
            total_weight += w
    return mst, total_weight

n = 5

edges = [
    (1,0,1),
    (3,0,2),
    (2,1,2),
    (4,1,3),
    (5,2,3),
    (7,3,4),
    (6,2,4)
]

mst, total = kruskal(n, edges)
print("Edges in mst: ", mst)
print("Total weight:", total)