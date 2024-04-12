class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end_of_word = True

    def find_min_input(self, word):
        node = self.root
        count = 0
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            count += 1
            if node.count == 1:  
                break
        return count

def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    total_input = 0
    for word in words:
        total_input += trie.find_min_input(word)
    
    return total_input
