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
    y = z.left
    t3 = y.right

    y.right = z
    z.left = t3
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def left_rotate(z):
    y = z.right
    t2 = y.left

    y.left = z
    z.right = t2
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def find_min(root):
    while root.left:
        root = root.left
    return root

def insert(root, data):
    if not root:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    
        
    root.height = 1+ max(height(root.left), height(root.right))
    bal = balance(root)

    if bal > 1 and data < root.left.data:
        return right_rotate(root)
    if bal < -1 and data > root.right.data:
        return left_rotate(root)
    
    if bal > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if bal < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

def delete(root, data):
    if not root:
        return None
    
    if data < root.data:
        root.left = delete(root.left, data)
    elif data> root.data:
        root.right = delete(root.right, data)
    
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    # return root 

    root.height = 1 + max(height(root.left), height(root.right))
    bal = balance(root)

    if bal > 1 and balance(root.left) >= 0:
        return right_rotate(root)
    if bal > 1 and balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if bal < -1 and balance(root.right) <= 0:
        return left_rotate(root)
    if bal < -1 and balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

def level_order_traversal(root):
    if not root:
        return None
    
    queue = deque([root])
    # queue.append()

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()

def print_tree(node, levl=0, prefix="Root:"):
    if node:
        print("    "*levl + prefix + str(node.data))
        print_tree(node.left, levl+1, "L---")
        print_tree(node.right, levl+1, "R---")

root = None
for val in [10, 20, 30, 40, 50, 25]:
    root = insert(root, val)

print_tree(root)
print("Level order before deletion:")
level_order_traversal(root)

root = delete(root, 40)
print("After deleting 40:")
level_order_traversal(root)

root = delete(root, 30)
print("After deleting 30:")
level_order_traversal(root)

root = delete(root, 50)
print("After deleting 50:")
level_order_traversal(root)
print_tree(root)