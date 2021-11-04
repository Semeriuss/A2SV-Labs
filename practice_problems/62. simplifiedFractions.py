from typing import List


class Solution:
    def gcd(self, a,b):
        if a%b == 0:
            return b
        return self.gcd(b, a%b)
    
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n):
            for j in range(i+1, n+1):
                if self.gcd(i, j) == 1:
                    ans.append(f'{i}/{j}')
        return ans

print(Solution().simplifiedFractions(4))