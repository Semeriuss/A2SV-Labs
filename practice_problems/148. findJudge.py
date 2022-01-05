from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdegree = [0 for _ in range(n)]
        
        for a, b in trust:
            outdegree[a - 1] -= 1
            outdegree[b - 1] += 1
            
        for p, c in enumerate(outdegree):
            if c == n - 1:
                return p + 1
        return -1
    
n = 3
trust = [[1,2], [2,3]]

# n = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

print(Solution().findJudge(n, trust))