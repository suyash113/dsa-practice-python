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

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
preorder(root)
print("preorder:\n")

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
inorder(root)
print("inorder:\n")

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
postorder(root)
print("postorder:\n")