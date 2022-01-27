from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = {}
        maxbits = len(bin(max(nums))) - 2
        maxor = 0
        for num in nums:
            num_in_bin = bin(num).lstrip('0b')
            if len(num_in_bin) < maxbits: num_in_bin = '0'*(maxbits - len(num_in_bin)) + num_in_bin
            current, operation = trie, trie
            for bit in num_in_bin:
                desired = int(not int(bit))
                if str(desired) in operation: operation = operation[str(desired)]
                elif str(int(not desired)) in operation: operation = operation[str(int(not desired))]
                if bit not in current: current[bit] = {}
                current = current[bit]
            current['#'] = num
            if '#' in operation: 
                maxor = max(maxor, num^operation['#'])
        return maxor
    
nums = [3, 25, 10, 5, 2, 8]
print(Solution().findMaximumXOR(nums))
        