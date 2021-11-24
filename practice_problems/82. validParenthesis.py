class Solution:
    def isValid(self, s: str) -> bool:
        opener = {'(': ')', '{': '}', '[':']'}
        stack = []
        for b in s:
            if b in opener:
                stack.append(b)
            else:
                if not stack:
                    return False
                if opener[stack.pop()] != b:
                    return False
        return True

s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
s = "{[]}"
print(Solution().isValid(s))