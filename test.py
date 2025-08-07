from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initially height = 1 (not 0)

# Height utility
def height(node):
    return node.height if node else 0

# Balance factor
def get_balance(node):
    return height(node.left) - height(node.right) if node else 0

# Right rotate
def right_rotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

# Left rotate
def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

# Get min value node (for deletion)
def get_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Insert into AVL
def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # Duplicates not allowed

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    # Balancing
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    lef_dt = root.left.key
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Delete from AVL
def delete(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node to delete
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            temp = get_min_value_node(root.right)
            root.key = temp.key
            root.right = delete(root.right, temp.key)

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))

    # Balance
    balance = get_balance(root)

    # Balancing cases
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Level Order Traversal
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.key, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()

# Test
root = None
for val in [10, 20, 30, 40, 50, 25]:
    root = insert(root, val)

print("Level order before deletion:")
level_order(root)

# Deleting nodes
root = delete(root, 40)
print("After deleting 40:")
level_order(root)

root = delete(root, 30)
print("After deleting 30:")
level_order(root)

root = delete(root, 50)
print("After deleting 50:")
level_order(root)
