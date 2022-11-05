from collections import Counter 

def solve(arr, k):
    req = []
    for num in arr:
        if num % k != 0:
            req.append(k - num%k)
        else:
            req.append(0)
    
    rem = Counter(req)
    steps = sorted(rem.items(), key=lambda x : (-x[1], -x[0])) 

    # print(rem, steps)
    maxStep, maxAmount = 0, 0
    for amount, step in steps:
        if step != 0 and amount != 0:
            maxStep = step
            maxAmount = amount
            break 
    
    if maxAmount == 0 or maxStep == 0:
        return 0
    
    res =  maxAmount + (maxStep - 1)*k
    return res + 1


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, k))