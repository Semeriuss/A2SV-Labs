def reverseInteger(num):
    negativeFlag = False
    if num < 0:
        negativeFlag = True
        num *= -1
    if 0 < num < 9:
        return num

    reversedNum = 0
    
    while num > 9:
        reversedNum += num%10
        num //= 10
        reversedNum *= 10
    reversedNum += num

    if (reversedNum < pow(-2, 31) or reversedNum > pow(2, 31)-1):
        return 0

    return reversedNum if not negativeFlag else reversedNum * -1
        

tests = [(0, 0),
         (123, 321),
         (112, 211),
         (7126, 6217),
         (-123, -321),
         (120, 21)]

for test in tests:
    num, expected = test
    actual = reverseInteger(num)
    print(actual == expected, actual, expected)
         
    
