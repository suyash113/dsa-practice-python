from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def build_tree():
    root_val = input("Enter the root node value: ")
    if root_val.lower() == "none":
        return None
    root = Node(root_val)
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        
        left_val= input(f"Enter left child of {current.data} or none: ")
        if left_val.lower() != "none":
            current.left = Node(left_val)
            queue.append(current.left)
        
        right_val= input(f"Enter right child of {current.data} or none: ") 
        if right_val.lower() != "none":
            current.right = Node(right_val)
            queue.append(current.right)
        
    return root

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
print("preorder\n")        
preorder(build_tree())

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
print("\nlevel order")
level_order(build_tree())