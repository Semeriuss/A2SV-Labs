class Solution:
    def decodeString(self, s: str) -> str:
        
        curnum = 0
        stack = []
        curstring = ""

        for c in s:
            if c == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ""
                curnum = 0
            
            elif c == ']':
                count = stack.pop()
                prevstring = stack.pop()
                curstring = prevstring + curstring*count
            
            elif c.isdigit():
                curnum = curnum*10 + int(c)
            
            else:
                curstring += c

        return curstring

s = "3[a2[c]2[d]]"
# s = "3[a2[c]]"
print(Solution().decodeString(s))

