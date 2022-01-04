def solve(n, l, r):
    path = []

    def pulverize(n):
        nonlocal path
        if n == 0 or n == 1:
            return n
        
        pulverized1 = pulverize(n//2)
        mod = n%2
        pulverized2 = pulverize(n//2)
        path.extend([pulverized1, mod, pulverized2])
        return pulverized2
    ans = pulverize(n)
    return path if path else [ans]
    


if __name__ == "__main__":
    n, l, r = map(int, input().split())
    print(solve(n, l, r))