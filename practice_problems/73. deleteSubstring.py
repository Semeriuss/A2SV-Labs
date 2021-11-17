def deleteSubstring(s, k):
    
    stack = []
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])
        
        if stack and stack[-1][1] == k:
            stack.pop()
    
    return "".join(char * occurrence for char, occurrence in stack)

print(deleteSubstring("ddbbcccbdaaa", 3))