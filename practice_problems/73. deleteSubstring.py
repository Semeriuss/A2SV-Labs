def deleteSubstring(s, k):
    start, end = 0, 0
    count = 0
        
    while end < len(s) or len(s) < k:
        if count == k:            
            s.replace(s[start]*k, "") 
     
            start, end = 0, 0
            
        if s[start] == s[end]:
            end += 1
            count += 1
        else:
            start = end
            count = 0
            end += 1
            
    return s
print(deleteSubstring("ddbbcccbdaa", 3))