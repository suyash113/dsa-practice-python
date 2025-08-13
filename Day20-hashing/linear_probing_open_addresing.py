class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
        self.tomstone = "<deleted>"
        
    def hash_function(self, key):
        index  = sum(ord(c) for c in key)%self.size
        return index
    
    def insert(self, key, value):
            index = self.hash_function(key)
            original_index = index
            while self.table[index] is not None and self.table[index][0] != key:
                index = (index + 1) % self.size
                if index == original_index:
                    raise Exception("Hash table is full")
            self.table[index] = (key, value)


    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index]:
            if self.table[index][0] == key:
                return self.table[index][1]
            index =(index+1)%self.size
            if index == start_index:
                break
        return False
    
    def delete(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index] = None
            index =(index+1)%self.size
            if index == start_index:
                break
            
    
    def display(self):
            for i, item in enumerate(self.table):
                print(f"Index {i}: {item}")

ht = LinearProbingHashTable(5)
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