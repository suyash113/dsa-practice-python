# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [None]*size
    
#     def hash_function(self, key):
#         index = sum(ord(c) for c in key)%self.size
#         return index

#     def insert(self,key, value):
#         index = self.hash_function(key)
#         new_node = Node(key, value)

#         if not self.table[index]:
#             self.table[index] = new_node
#         else:
#             current = self.table[index]
#             while True:
#                 if current.key == key:
#                     current.value = value
#                 if current.next is None:
#                     break
#                 current = current.next
#             current.next = new_node

#     def search(self, key):
#         index = self.hash_function(key)
#         current = self.table[index]
#         while current:
#             if current.key == key:
#                 return True
#             else:
#                 current = current.next
#         return False
    
#     def delete(self, key):
#         index = self.hash_function(key)
#         current = self.table[index]
#         prev = None
#         while current:
#             if current.key == key:
#                 if prev:
#                     prev.next = current.next 
#                 else:
#                     self.table[index] = current.next 
#                 return True
#             prev = current
#             current = current.next
#         return False
    
#     def display(self):
#         for i in range(self.size):
#             print(f"{i}", end=" ")
#             current = self.table[i]
#             while current:
#                 print(f"({current.key}, {current.value})", end="->")
#                 current = current.next
#             print("None")

# ht = HashTable(5)
# ht.insert("cat", 10)
# ht.insert("dog", 20)
# ht.insert("tiger", 30)
# ht.insert("monkey", 40)
# ht.insert("god", 50)

# ht.display()
# print("\n")
# print("search dog", ht.search("dog"))
# print("\n")
# print("Delete cat", ht.delete("cat"))
# print("\n")
# ht.display()






class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
    
    def hash_function(self, key):
        return sum(ord(c) for c in key)%self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)

        if not self.table[index]:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                if current.next is None:
                    break
                else:
                    current = current.next
            current.next = new_node
        
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key:
                return True
            else:
                current = current.next
        return False
    
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next 
                return True
            prev = current
            current = current.next
        return False
    
    def display(self):
        for i in range(self.size):
            print(f"{i}", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}, {current.value})", end="->")
                current = current.next
            print("None")

ht = HashTable(5)
ht.insert("cat", 10)
ht.insert("dog", 20)
ht.insert("tiger", 30)
ht.insert("monkey", 40)
ht.insert("god", 50)

ht.display()
print("\n")
print("search dog", ht.search("dog"))
print("\n")
print("Delete cat", ht.delete("cat"))
print("\n")
ht.display()