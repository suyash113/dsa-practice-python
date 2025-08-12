class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True
    
    def search(self, word):
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return current.is_end
    
    def prefix(self, prefixx):
        current = self.root
        for char in prefixx:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True

def delete(root, word, index=0):
    char = word[index]
    current = root.children.get(char)
    nodetoDelete = False

    if len(current.children) >1:
        delete(current, word, index+1)
        return False
    
    if index == len(word)-1:
        if len(current.children) >=1:
            return False
        else:
            root.children.pop(char)
            return True
        
    if current.is_end == True:
        delete(current, word, index+1)
        return True
    
    nodetoDelete = delete(current, word, index+1)
            


trie = Trie()
words = ["cat", "cap", "can", "dog"]
# for _ in words:
#     trie.insert(words.pop())

print(trie.insert("cat"))
print(trie.insert("dog"))
print(trie.insert("car"))
print(trie.insert("can"))

print(trie.search("cat"))
print(trie.search("dog"))
print(trie.search("car"))
print(trie.search("cad"))

print(trie.prefix("ca"))
print(trie.prefix("do"))
print(trie.prefix("x"))