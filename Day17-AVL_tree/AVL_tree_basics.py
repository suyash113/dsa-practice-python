from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def height(root):
    if not root:
        return 0
    return root.height

def balance(root):
    if not root:
        return 0
    return height(root.left) - height(root.right)

def right_rotate(z):
    y = z.left                  #   z
    t3 = y.right                #  /
                                # y        y
    y.right = z                # /        / \
    z.left = t3               # x        x   z
              
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def left_rotate(z):
    y = z.right                 #z
    t2 = y.left                 # \            
                                #  y          y       
    y.left = z                  #   \        / \      
    z.right = t2                #    x      z   x     

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def insert(root, data):
    if not root:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    
    root.height = 1 + max(height(root.left), height(root.right))
    bal = balance(root)

    if bal > 1 and data < root.left.data:
        return right_rotate(root)

    if bal > 1 and data > root.right.data:
        return left_rotate(root)

    if bal > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if bal < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def print_tree(node, levl=0, prefix="Root:"):
    if node:
        print("    "*levl + prefix + str(node.data))
        print_tree(node.left, levl+1, "L---")
        print_tree(node.right, levl+1, "R---")

root = None
for val in [30, 20, 40, 10, 25, 50,5]:
    root = insert(root, val)

print_tree(root)