from typing import List


class Solution:
    # O(2^N) time and O(n) | where n is the number of parenthesis generated
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(left, right, path, res):
            if left == 0 and right == 0:
                res.append(path[:])
            if left:
                dfs(left - 1, right + 1, path + "(", res)
            if right:
                dfs(left, right - 1, path + ")", res)

        res = []
        dfs(n, 0, "", res)
        return res
