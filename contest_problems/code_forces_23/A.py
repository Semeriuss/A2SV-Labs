def solve(arr):
    mx = 1
    count = 1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            mx = max(mx, count)
            count = 0
        count += 1
    mx = max(mx, count)
    return mx

input()
print(solve(list(map(int, input().split()))))