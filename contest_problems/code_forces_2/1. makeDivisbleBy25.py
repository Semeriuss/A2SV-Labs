import sys

input = sys.stdin.readline
n = int(input())

tests = []
for i in range(n):
    input = sys.stdin.readline
    tests.append(int(input()))
 
def _helper(num, count):
    # print("count", count, "num", num)
    if num % 25 == 0:
        return count
    if num < 25:
        return count
    # print("hherere", int(str(num)[len(str(num))-1:]))
    if int(str(num)[len(str(num))-1:]) == 0:
        # print("checkereeer", int(str(num)[len(str(num))-2:len(str(num))-1]))
        if int(str(num)[len(str(num))-2:len(str(num))-1]) == 0 or int(str(num)[len(str(num))-2:len(str(num))-1]) == 5:
            return count
        else:
            # print("here", num)
            count += 1
            num = int(str(num)[:len(str(num))-2] + str(num)[len(str(num))-1:])
            # print("after here", num)
            return _helper(num, count)
    elif int(str(num)[len(str(num))-1:]) == 5:
        # print("checkereeer", int(str(num)[len(str(num))-2:len(str(num))-1]))
        if int(str(num)[len(str(num))-2:len(str(num))-1]) == 2 or int(str(num)[len(str(num))-2:len(str(num))-1]) == 7:
            return count
        elif int(str(num)[len(str(num))-2:len(str(num))-1]) == 0:
            if len(str(num)) >= 3 and int(str(num)[len(str(num))-3:len(str(num))-2]) == 0 or int(str(num)[len(str(num))-3:len(str(num))-2]) == 5:
                count += 1
                num = int(str(num)[:len(str(num))-1])
                return _helper(num, count)
        else:
            # print("here", num)
            count += 1
            num = int(str(num)[:len(str(num))-2] + str(num)[len(str(num))-1:])
            # print("after here", num)
            return _helper(num, count)
    else:
        count += 1
        num = int(str(num)[:len(str(num))-1])
        return _helper(num, count)
    


def makeDivisibleBy25(num):
    count = 0
    return _helper(num, count)


for test in tests:
    print(makeDivisibleBy25(test))

