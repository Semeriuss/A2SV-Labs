def maximumIncrease(nums):
    length = 0

    sp = 0
    ep = 1

    currLength = 0
    while ep < len(nums):
        if nums[sp] < nums[ep]:
            currLength += 1

        elif nums[sp] >= nums[ep]:
            currLength = 0
            
        sp = ep
        ep += 1
        length = max(length, currLength)      
    return length + 1

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    print(maximumIncrease(nums))