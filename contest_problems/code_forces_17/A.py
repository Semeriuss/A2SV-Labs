def solve(a, b):
    def calculate(x, y):
        total = 0
        for i in range(len(x) - 1):
            total += abs(x[i] - x[i + 1]) + abs(y[i] - y[i + 1])
        return total
    
    minArr, maxArr = [], []
    for i in range(len(a)):
        minArr.append(min(a[i], b[i]))
        maxArr.append(max(a[i], b[i]))
    
    return calculate(minArr, maxArr)

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        res.append(solve(a, b))
    print(*res)