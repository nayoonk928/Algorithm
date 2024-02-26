from collections import deque

def can_transform(word1, word2):
    diff_count = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = set()
    queue = deque([(begin, 0)])  # (word, depth)

    while queue:
        current_word, depth = queue.popleft()

        if current_word == target:
            return depth

        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                queue.append((word, depth + 1))

    return 0