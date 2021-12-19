from typing import List

def overlaps(window1, window2):
    openBoundary1, closeBoundary1 = window1
    openBoundary2, closeBoundary2 = window2

    if openBoundary1 <= openBoundary2 <= closeBoundary1 <= closeBoundary2:
        return True
    elif openBoundary2 <= openBoundary1 <= closeBoundary2 <= closeBoundary1:
        return True
    elif openBoundary2 <= openBoundary1 <= closeBoundary1 <= closeBoundary2:
        return True
    else:
        return False

def maxSumTwoNoOverlap(nums: List[int], firstLen: int, secondLen: int) -> int:
        maxSum1 = 0
        maxSum2 = 0

        finalMaxSum = 0

        firstLen, secondLen = (firstLen, secondLen) if firstLen < secondLen else (secondLen, firstLen)

        firstLenOpener = 0
        firstLenCloser = 0 + firstLen

        secondLenOpener = 0
        secondLenCloser = 0 + secondLen

        for i in range(len(nums) - firstLen):
            maxSum1 = sum([nums[pos + i] for pos in range(firstLen)])
            firstLenOpener = i
            firstLenCloser = i + firstLen - 1
            for i in range(len(nums) - secondLen):
                secondLenOpener = i
                secondLenCloser = i + secondLen - 1
                if not overlaps((firstLenOpener, firstLenCloser), (secondLenOpener, secondLenCloser)):
                    maxSum2 = sum([nums[pos + i] for pos in range(secondLen)])
                    secondLenOpener = i
                    secondLenCloser = i + secondLen - 1
                print(nums[firstLenOpener : firstLenCloser + 1], nums[secondLenOpener : secondLenCloser + 1], maxSum1 + maxSum2)
            finalMaxSum = max(finalMaxSum, maxSum1 + maxSum2)
        
        return finalMaxSum

tests = [([0,6,5,2,2,5,1,9,4], 1, 2), 
        ([3,8,1,3,2,1,8,9,0], 3, 2), 
        ([2,1,5,6,0,9,5,0,3,8], 4, 3),
        ([0,6,5,2,2,5,1,9,4], 1, 2),
        ([3,8,1,3,2,1,8,9,0], 3, 2),
        ([2,1,5,6,0,9,5,0,3,8], 4, 3),
        ([0,6,5,2,2,5,1,9,4], 3, 2),
        ([3,8,1,3,2,1,8,9,0], 4, 3)]

tests = [([8,20,6,2,20,17,6,3,20,8,12], 5, 4)]
for test in tests:
    nums, firstLen, secondLen = test
    print(maxSumTwoNoOverlap(nums, firstLen, secondLen))



