# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode()
#             node = node.children[ch]
#         node.is_end = True
    
    # def search(self, word):
    #     current = self.root
    #     for char in word:
    #         if char in current.children:
    #             current = current.children[char]
    #         else:
    #             return False
    #     return current.is_end

#     def delete(self, word):
#         def _delete(node, word, depth):
#             if not node:
#                 return False

#             if depth == len(word):
#                 if not node.is_end:
#                     return False
#                 node.is_end = False
#                 return len(node.children) == 0

#             ch = word[depth]
#             should_delete_child = _delete(node.children[ch], word, depth + 1)

#             if should_delete_child:
#                 del node.children[ch]
#                 return not node.is_end and len(node.children) == 0

#             return False

#         _delete(self.root, word, 0)

# trie = Trie()

# print(trie.insert("cat"))
# print(trie.insert("APIS"))
# print(trie.insert("AP"))
# print(trie.insert("can"))

# print(trie.delete("AP"))
# # print(trie.search("AP"))


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

    def delete(self, word):
        def _delete(node, word, index):
            if not node:
                return False

            if index == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
        
            ch = word[index]
            nodeToDelete = _delete(node.children[ch], word, index+1)

            if nodeToDelete:
                del node.children[ch]
                return not node.is_end and len(node.children) == 0
            return False
            
        _delete(self.root, word, 0)

trie = Trie()

print(trie.insert("cat"))
print(trie.insert("APIS"))
print(trie.insert("AP"))
print(trie.insert("can"))

print(trie.delete("AP"))
print(trie.search("AP"))