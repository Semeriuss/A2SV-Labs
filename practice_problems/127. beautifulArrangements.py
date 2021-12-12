from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        return self.fastCount(set(range(1, n + 1)), n)

    def fastCount(self, nums, i):
        if i == 1:
            return 1
        return sum(self.fastCount(nums - {remNums}, i - 1) for remNums in nums if not remNums % i or not i % remNums)


print(Solution().countArrangement(15))