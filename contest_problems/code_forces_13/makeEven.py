def makeEven(num):
    digits = str(num)

    if num % 2 == 0:
        return 0
    
    if int(digits[0]) % 2 == 0:
        return 1
    
    for digit in digits:
        if int(digit) % 2 == 0:
            return 2
    
    return -1

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        res.append(makeEven(int(input())))
    print(*res, sep="\n")
