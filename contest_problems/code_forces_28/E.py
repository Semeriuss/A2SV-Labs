for _ in range(int(input())):
    n = int(input())
    s = input()

    res = 0
    b = [0] * (n + 1)
    b[0] = bal = n 
    for i in range(1, n + 1):
        if s[i - 1] == '+':
            bal += 1
        else:
            bal -= 1
        
        b[i] = bal
        for j in range(i):
            if b[j] >= b[i] and (b[j] - b[i]) % 3 == 0:
                res += 1
    
    print(res)
