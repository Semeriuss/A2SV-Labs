t = int(input())

tests = []
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    tests.append((n, nums))

def hasPermutation(n, nums):

    sp = 0
    mp = 1
    ep = 2

    permutationExists = False
    permutation = ""

    while ep < n:
        if nums[sp] > nums[mp] or nums[ep] > nums[mp]:
            sp += 1
            mp += 1
            ep += 1
        
        if ep < n and nums[ep] >= nums[mp]:
            ep += 1
        
        if ep < n and nums[sp] < nums[mp] and nums[ep] < nums[mp]:
            permutationExists = True
            permutation = f'{sp + 1} {sp + 2} {ep + 1}'
            break
    
    if not permutationExists:
        ep = mp + 1
        while mp < n:
            if ep >= n:
                mp += 1
                ep = mp + 1

            if ep < n and nums[mp] < nums[ep]:
                ep += 1
            
            if ep < n and nums[mp] > nums[ep]:
                permutationExists = True
                permutation = f'{sp + 1} {mp + 1} {ep + 1}'
                break


    if permutationExists:
        print("YES")
        print(permutation)
    else:
        print("NO")

for test in tests:
    n, nums = test
    hasPermutation(n, nums)


