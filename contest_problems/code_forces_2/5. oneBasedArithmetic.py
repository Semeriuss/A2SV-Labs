import sys

input = sys.stdin.readline
num = int(input())

def _helper(num, count):
    if num == 0:
        return count
    
    n = len(str(num)) if num > 0 else len(str(num)) - 1
    if n == 1:
        if num > 6:
            num -= 11
            count += 2
            return _helper(num, count)
        elif 0 < num <= 6:
            num -= 1
            count += 1
            return _helper(num, count)
        elif num < -6:
            num += 11
            count += 2
            return _helper(num, count)
        else:
            num += 1
            count += 1
            return _helper(num, count)
    else:
        if num > 0:
            toSubtract = int("".join(["1" for i in range(n)])) if abs(num - int("".join(["1" for i in range(n)]))) < abs(num - int("".join(["1" for i in range(n + 1)]))) else int("".join(["1" for i in range(n + 1)]))
            num -= toSubtract
            count += len(str(toSubtract))
            return _helper(num, count)
        else:
            toAdd = int("".join(["1" for i in range(n)])) if abs(num - int("".join(["1" for i in range(n)]))) < abs(num - int("".join(["1" for i in range(n + 1)]))) else int("".join(["1" for i in range(n + 1)]))
            num += toAdd
            count += len(str(toAdd))
            return _helper(num, count)


def oneBasedArithmetic(num):
    if num == 0:
        return 2
    count = 0
    return _helper(num, count)


print(oneBasedArithmetic(num))
