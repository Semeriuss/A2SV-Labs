def goodnums(n):
    count = 1
    visited = set()
    for num in range(2, int(pow(n, 0.5)) + 1):
        if num**2 < n+1 and num**2 not in visited:
            count += 1
            visited.add(num**2)
        if num**3 < n+1 and num**3 not in visited:
            count += 1
            visited.add(num**3)
    return count

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
       res.append((goodnums(int(input()))))
    print(*res)
        