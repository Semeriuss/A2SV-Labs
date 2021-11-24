from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, invalid, target, visited, possibles):
            hashmap = {}
            for i, num in enumerate(nums):
                if num in hashmap and i != invalid and hashmap[num] != invalid:
                    # print(0 - target, nums[hashmap[num]], "====i====", hashmap[num], "invalid", invalid, " ", nums[i])
                    possible = sorted([0 - target, nums[hashmap[num]], nums[i]])
                    toVisit = tuple(possible)
                    if toVisit not in visited:
                        visited.add(toVisit)
                        possibles.append(possible)
                hashmap[target - num] = i
            return possibles
        
        res = []
        visited = set()        
        for i, num in enumerate(nums):
            res = twoSum(nums, i, 0 - num, visited, res)         
        return res

# test = [-1,0,1,0,2,-1,1,0,2,-1,1,0,2,-1,0,2,-4,-1,0,1,0,2]
test = [-1,0,1,2,-1,-4]
test = [0, 0]
print(Solution().threeSum(test))