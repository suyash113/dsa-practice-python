from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

def insert(root, data):
    if not root:
        root = Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def height(root):
    if not root:
        return 0
    high=0 
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        high += 1
    return high

def max(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.data
def min(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.data
    
    # if root.right:
    #     root.right = height(root.right, high+1)
    # if root.left:
    #     root.left = height(root.left, high+1)
    # return high
    
for v in values:
    root = insert(root, v)
insert(root, 2)
insert(root, 15)

print("Inorder Traversal (Sorted):")
inorder(root)  # 1 3 4 6 7 8 10 13 14
print(height(root))
print(max(root))
print(min(root))