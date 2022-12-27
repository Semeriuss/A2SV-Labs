from collections import Counter, defaultdict
s = input()
t = input()
n = len(s)
m = len(t)

automaton = needTree = False 
slist = list(s)
tCount = Counter(list(t))
sCount = Counter(list(s))
for i in range(0, n):
    if tCount[s[i]] > 0:
        tCount[s[i]] -= 1
    else:
        automaton = True

j = 0
for i in range(0, n):
    if j >= m or s[i] != t[j]:
        slist[i] = ""
    else:
        j += 1

for i in range(0, m):
    if sCount[t[i]] > 0:
        sCount[t[i]] -= 1
    else:
        needTree = True 
        break 

if needTree:
    print("need tree")
elif all(not frequencyT for frequencyT in tCount.values()) and "".join(slist) == t:
    print("automaton")
else:
    tChars = Counter(list(t))
    sChars = defaultdict(int)
    for c in s:
        if c not in tChars:
            automaton = True 
        sChars[c] += 1
    
    if automaton:
        print("both")
    else:
        print("array")

    


