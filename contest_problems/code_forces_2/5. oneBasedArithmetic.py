import sys

input = sys.stdin.readline
num = int(input())

def _helper(num, count):
    if num == 0:
        return count
    
    n = len(str(num)) if num > 0 else len(str(num)) - 1
    if n == 1:
        if num > 5:
            num -= 11
            count += 2
            return _helper(num, count)
        elif 0 < num <= 5:
            num -= 1
            count += 1
            return _helper(num, count)
        elif num < -5:
            num += 11
            count += 2
            return _helper(num, count)
        else:
            num += 1
            count += 1
            return _helper(num, count)
    else:
        if num > 0:
            num -= int("".join(["1" for i in range(n)]))
            count += n
            return _helper(num, count)
        else:
            num += int("".join(["1" for i in range(n)]))
            count += n
            return _helper(num, count)


def oneBasedArithmetic(num):
    if num == 0:
        return 1
    if len(set(list(str(num)))) == 1 and str(num)[0] == '1':
        return 0
    count = 0
    return _helper(num, count)


print(oneBasedArithmetic(num))
