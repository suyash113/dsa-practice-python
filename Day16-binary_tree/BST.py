class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    
def insert(root, data):
    if not root:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


def search(root, data):
    if not root:
        return False
    if root.data == data:
        return True
    
    if data < root.data:
        return(search(root.left, data))
    else:
        return (search(root.right, data))
    
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Create BST
for v in values:
    root = insert(root, v)
insert(root, 2)
insert(root, 15)

print("Inorder Traversal (Sorted):")
inorder(root)  # 1 3 4 6 7 8 10 13 14

print("\nSearch for 6:", search(root, 6))  # True
print("Search for 20:", search(root, 20))  # False
