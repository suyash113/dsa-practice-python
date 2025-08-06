class Node:                    #class fot node for crearing binary tree left & right
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# create tree with nodes example

root = Node("A")
root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

    #         A
    #       /   \
    #      B     C      THIS IS TREE STUCTURE
    #     / \     \
    #    D   E     F
# for Depth First Search [DFS] 3 types

from collections import deque

def level_order(root):
    if not root:
        return None
    
    queue = deque()
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
print("Level order:")
level_order(root)