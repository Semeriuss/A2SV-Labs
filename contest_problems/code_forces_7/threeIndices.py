t = int(input())

tests = []
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    tests.append((n, nums))

def hasPermutation(n, nums):

    sp = 0
    ep = 1

    permutationExists = False
    permutation = ""

    if n < 2:
        return 0

    for i in range(1, n - 1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1] :
            print("YES")
            return f'{i} {i + 1} {i + 2}'
     
    return "NO"

for test in tests:
    n, nums = test
    print(hasPermutation(n, nums))


