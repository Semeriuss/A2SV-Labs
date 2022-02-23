def findX(y, k, n):
    if y >= n: return [-1]
    res = []
    factor = k
    while factor <= n:
        if factor - y > 0: res.append(factor - y)
        factor += k
    return res if res else [-1]

if __name__ == '__main__':
    y, k, n = map(int, input().split())
    ret = findX(y, k, n)
    print(*ret)
