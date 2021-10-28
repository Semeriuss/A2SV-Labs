class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0: return -1

        length = 0
        for i in range(k):
            length = (length * 10 + 1) % k
            if length == 0:
                return i + 1
        return -1

print(Solution().smallestRepunitDivByK(99999))