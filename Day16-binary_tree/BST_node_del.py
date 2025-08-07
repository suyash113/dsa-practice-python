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

def search(root, data):
    if not root:
        return False
    if root.data == data:
        return True
    
    if data < root.data:
        return(search(root.left, data))
    else:
        return(search(root.right, data))

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# def find_min(node):
#     while node.left:
#         node = node.left
#     return node

# def delete(root, data):
    # if not root:
    #     return None
    
    # if data < root.data:
    #     root.left = delete(root.left, data)
    # elif data > root.data:
    #     root.right = delete(root.right, data)
    
    # else:
    #     if not root.left and not root.right:
    #         return None
    #     elif not root.left:
    #         return root.right
    #     elif not root.right:
    #         return root.left
        
    #     temp = find_min(root.right)
    #     root.data = temp.data
    #     root.right = delete(root.right, temp.data)
    # return root 
    
def find_min(node):
    while node.left:
        node = node.left
    return node
def delete(root, data):
    if not root:
        return None
    
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    
    else:
        if not root.left and not root.right:
            return None
        elif not root.left:
            return(root.right)
        elif not root.right:
            return(root.left)
        
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

for v in values:
    root = insert(root, v)
insert(root, 2)
insert(root, 15)

print("Inorder Traversal (Sorted):")
inorder(root)  # 1 3 4 6 7 8 10 13 14

print(delete(root, 6))

print("Inorder Traversal (Sorted):")
inorder(root) 