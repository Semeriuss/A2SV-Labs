class Solution:
    def isValid(self, s: str) -> bool:
        opener = {'(': ')', '{': '}', '[':']'}
        stack = []
        for b in s:
            if b in opener:
                stack.append(b)
            elif not stack:
                return False
            elif opener[stack.pop()] != b:
                return False
        return True if len(stack) == 0 else False

s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
s = "{[]}"
s = "["
s = "]"
print(Solution().isValid(s))