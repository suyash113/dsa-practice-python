class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def print_tree(self, level=0):
        print(" "*level*2+str(self.data))
        for child in self.children:
            child.print_tree(level+1)

    def print_tree_iterative_dfs(root):
        stack = [(root, 0)]  # Each item is (node, level)

        while stack:
            node, level = stack.pop()
            print(' ' * level * 2 + str(node.data))

            # Push children in reverse so leftmost child is processed first
            for child in reversed(node.children):
                stack.append((child, level + 1))

root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

root.add_child(b)
root.add_child(c)
b.add_child(d)

root.print_tree()
root.print_tree_iterative_dfs()


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def print_tree(self, level=0):
        print("  "*level + str(self.data))
        for child in self.children:
            child.print_tree(level+1)

root = Node("A")
ch1 = Node("B")
ch2 = Node("C")

root.add_child(ch1)
root.add_child(ch2)

ch1.add_child(Node("D"))
ch1.add_child(Node("E"))
ch2.add_child(Node("F"))

root.print_tree()