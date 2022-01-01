from typing import List

class LargeNumKey(str):
    def __lt__(x, y):
        return x + y < y + x

def largestNumber(nums: List[int]) -> str:
    return "".join(sorted(map(str, nums), reverse=True, key=LargeNumKey))
   
        

print(largestNumber([3,30,34,5,9]))