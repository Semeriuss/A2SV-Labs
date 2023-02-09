from typing import List


class Solution:
    # O(1) time and space
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        if n > 12:
            return []

        def backtrack(i, path):
            if i == n and len(path) == 4:
                res.append(path[:])
                return
            if len(path) > 4:
                return
            for j in range(i, min(i + 3, n)):
                tmp = s[i: j + 1]
                if 0 <= int(tmp) <= 255 and (i == j or s[i] != '0'):
                    backtrack(j + 1, path + [tmp])

        backtrack(0, [])
        return [".".join(seq) for seq in res]
