def deleteSubstring(s, k):
    
    stack = [[]]
    for char in s:
        if stack[-1] != [] and stack[-1][1] == k:
            stack.pop()
        if stack[-1] != [] and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])
    
    ans = []
    for sub in stack:
        if sub != []:
            ans.append(sub[0])
    
    return "".join(ans)
print(deleteSubstring("ddbbcccbdaa", 3))