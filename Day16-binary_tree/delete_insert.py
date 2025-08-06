from collections import deque

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
    
    
def delete(root, key):
    if not root:
        return None
    
    if not root.left and not root.right:
        if root.value == key:
            return None
        else:
            return root

    queue = deque([root])
    node_to_delete = None
    last_node = None
    parent_of_last = None

    while queue:
        last_node = queue.popleft()
        if last_node.value == key:
            node_to_delete = last_node
        if last_node.left:
            parent_of_last = last_node
            queue.append(last_node.left)
        if last_node.right:
            parent_of_last = last_node
            queue.append(last_node.right)

    if node_to_delete:
        node_to_delete.value = last_node.value
        if parent_of_last.right == last_node:
            parent_of_last.right = None
        else:
            parent_of_last.left = None

    return root


def insert(root, value):
    if not root:
        return Node(value)

    queue = deque([root])
    while queue:
        node = queue.popleft()

        # First empty left child
        if not node.left:
            node.left = Node(value)
            break
        else:
            queue.append(node.left)

        # First empty right child
        if not node.right:
            node.right = Node(value)
            break
        else:
            queue.append(node.right)

    return root
