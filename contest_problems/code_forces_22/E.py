s = input()
good = input()
k = int(input())

trie = {}
n, res = len(s), 0
for i in range(n):
    curr = trie
    credit = k
    for j in range(i, n):
        if good[ord(s[j]) - ord('a')] == '0' and credit <= 0:
            break
        if ord(s[j]) - ord('a') not in curr:
            curr[ord(s[j]) - ord('a')] = {}
            res += 1
        if good[ord(s[j]) - ord('a')] == '0': credit -= 1
        curr = curr[ord(s[j]) - ord('a')]
print(res)
            
