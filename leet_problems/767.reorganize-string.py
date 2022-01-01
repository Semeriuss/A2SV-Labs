#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        stack = []
        temp = []
        for letter in s:
            if not stack:
                stack.append(letter)
            elif stack and stack[-1] != letter:
                stack.append(letter)
            else:
                temp.append(letter)
            if temp and stack and temp[-1] != stack[-1]:
                stack.append(temp.pop())
        res = []
        for letter in stack:
            if res and res[-1] == letter:
                pass
            if temp and letter != temp[-1]:
                res.append(letter)
                res.append(temp.pop())
            else:
                res.append(letter)        
        ans = "".join(res)
        print(ans)
        return ans if len(ans) == len(s) else ""

# @lc code=end

