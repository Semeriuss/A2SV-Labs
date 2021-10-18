def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
    
        nums_dict = {}
        
        for i, num in enumerate(nums):
            if num in nums_dict and abs(nums_dict[num] - i) <= k:
                return True
            nums_dict[num] = i
        return False
                
def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
    
        nums_dict = {num : [] for num in nums}
        
        for i, num in enumerate(nums):
            if nums_dict[num] != [] and abs(nums_dict[num][0] - i) <= k:
                return True
            elif nums_dict[num] == []:
                nums_dict[num].append(i)
            else:
                nums_dict[num].pop()
                nums_dict[num].append(i)
        return False

tests = [([1,0,1,1],1),
         ([99,99], 2)]

for test in tests:
        nums, k = test
        print(containsNearbyDuplicate(nums, k))





















