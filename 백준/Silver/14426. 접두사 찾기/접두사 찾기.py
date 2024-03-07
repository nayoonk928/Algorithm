class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    
    def is_prefix(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# 입력 받기
N, M = map(int, input().split())
words_set = set(input().strip() for _ in range(N))
search_words = [input().strip() for _ in range(M)]

# trie 자료구조에 집합 S의 문자열들을 저장
trie = Trie()
for word in words_set:
    trie.insert(word)

# 접두사인지 판별하고 개수 세기
count = 0
for word in search_words:
    if trie.is_prefix(word):
        count += 1

# 결과 출력
print(count)
