from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = {}
        nums.sort(reverse=True)
        maxbits = len(bin(nums[0])) - 2
        
        for num in nums:
            num_in_bin = bin(num).lstrip('0b')
            if len(num_in_bin) < maxbits: num_in_bin = '0'*(maxbits - len(num_in_bin)) + num_in_bin
            current = trie
            for bit in num_in_bin:
                if bit not in current: current[bit] = {}
                current = current[bit]
            current['#'] = num

        maxor = 0
        for num in nums:
            num_in_bin = bin(num).lstrip('0b')
            if len(num_in_bin) < maxbits: num_in_bin = '0'*(maxbits - len(num_in_bin)) + num_in_bin
            current = trie
            for bit in num_in_bin:
                desired = int(not int(bit))
                if str(desired) in current: current = current[str(desired)]
                elif str(int(not desired)) in current: current = current[str(int(not desired))]
            if '#' in current: 
                maxor = max(maxor, num^current['#'])

        return maxor
    
nums = [3, 25, 10, 5, 2, 8]
print(Solution().findMaximumXOR(nums))
        