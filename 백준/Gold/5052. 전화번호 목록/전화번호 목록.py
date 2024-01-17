import sys

input = sys.stdin.readline


class Node:
    def __init__(self):
        self.data = {}
        self.leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for n in num:
            if n not in node.data:
                node.data[n] = Node()
            node = node.data[n]
        node.leaf = True

    def starts_with(self, prefix):
        node = self.root
        for n in prefix:
            if n not in node.data:
                return False
            node = node.data[n]
            if node.leaf:
                return True
        return False


def is_valid(phone_nums):
    trie = Trie()
    phone_nums = sorted(phone_nums)

    for num in phone_nums:
        if trie.starts_with(num):
            return "NO"
        trie.insert(num)

    return "YES"


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        phone_nums = [input().strip() for _ in range(n)]

        print(is_valid(phone_nums))