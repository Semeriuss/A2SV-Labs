from collections import Counter
for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    freq = Counter(nums)
    leftIndex = 0
    for i, num in enumerate(nums):
        if freq[num] > 1:
            leftIndex = i + 1
        freq[num] -= 1
    print(len(nums[:leftIndex]))

    