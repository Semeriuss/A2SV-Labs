class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0: return -1
        remainders = set()
        current_r = 1
        while current_r not in remainders:
            remainders.add(current_r)
            if current_r % k == 0:
                return len(list(str(current_r)))
            current_r *= 10
            current_r += 1
        return -1