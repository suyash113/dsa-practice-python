class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class LinkedList:
#     def __init__(self, data1):  # for making ll with at least 1 node
#         new_node = Node(data1)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

class LinkedList:
    def __init__(self):  # for making ll with no node
        self.head = None
        self.tail = None
        self.length = 0
        
        
new_linked_list = LinkedList(10)
print(new_linked_list.head.value)
        