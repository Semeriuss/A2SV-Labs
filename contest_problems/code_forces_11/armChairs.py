def armChairs(seats):
    stack = [[]]
    minutes = 0
    for i, seat in enumerate(seats):
        if stack[-1] == []:
            stack.append([seat, i])
        else:
            if stack[-1][0] != seat:
                val = stack.pop()
                minutes += (i - val[1])
            else:
                stack.append([seat, i])
    return minutes

if __name__ == "__main__":
    n = int(input())
    seats = list(map(int, input().split()))
    print(armChairs(seats))