import string

word = input()


result = [-1]*len(string.ascii_lowercase)
for i in range(len(word)):
    idx = ord(word[i]) - ord('a')
    if result[idx] == -1:
        result[idx] = i
print(' '.join([str(num) for num in result]))
