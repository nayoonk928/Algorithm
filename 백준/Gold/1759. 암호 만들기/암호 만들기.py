import sys
from collections import deque

input = sys.stdin.readline

password_length, c = map(int, input().split())
alphabet = list(input().split())

vowels = set('aeiou')

alphabet.sort()
queue = deque()

# 알파벳을 초기 노드로 큐에 추가
for char in alphabet:
    queue.append(char)

# bfs
while queue:
    current_node = queue.popleft()

    if len(current_node) == password_length:
        # 모음 개수 세기
        vowel_count = sum(1 for char in current_node if char in vowels)
        if 1 <= vowel_count <= password_length - 2:
            print("".join(current_node))
        continue

    last_char = current_node[-1] if current_node else None
    for char in alphabet:
        if not last_char or char > last_char:
            new_node = current_node + char
            queue.append(new_node)