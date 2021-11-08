t = int(input())

tests = []
for i in range(t):
    tests.append([int(char) for char in input()])

def ternaryString(nums):
    if len(set(nums)) != 3: 
        return 0
    
    sp = 0
    ep = 1
    numset = set([1, 2, 3])


    # numset.remove(nums[sp])
    while numset and ep < len(nums):
        if nums[sp] == nums[ep]:
            sp = ep
            

        if nums[ep] in numset:
            numset.remove(nums[ep])
            if not numset:
                break
        print(sp, ep, nums, numset)
        ep += 1

        
    
    
    return ep - sp
            

        
for test in tests:
    print(ternaryString(test))