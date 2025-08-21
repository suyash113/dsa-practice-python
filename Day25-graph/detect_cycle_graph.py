from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected

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
g.add_edge("C", "A")  # cycle A-B-C-A
print(g.graph)


print("Graph has cycle?", g.is_cyclic())  # ✅ True
