def unique(nums):
    visited = set()
    count = 0
    for num in nums:
        if num not in visited:
            count += 1
            visited.add(num)
        elif -num not in visited:
            count += 1
            visited.add(-num)
        
    return count

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        res.append(unique(nums))
    print(*res)