from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()

    counter = Counter(list(s))
    BALANCED = False
    l, r = 0, n - 1
    if counter['a'] != 0 and counter['b'] != 0:
        while l < r:
            if counter['a'] == counter['b']:
                BALANCED = True
                break
            if s[l] == s[r]:
                counter[s[l]] -= 1
                l += 1
            else:
                if counter[s[l]] < counter[s[r]]:
                    counter[s[r]] -= 1
                    r -= 1
                else:
                    counter[s[l]] -= 1
                    l += 1
        
    if BALANCED:
        print(l + 1, r + 1)
    else:
        print(-1, -1)
        
    