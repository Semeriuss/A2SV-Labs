def solve(weight, x):
    weight.sort()
    count = len(weight)
    left, right = 0, len(weight) - 1
    while left < right:
        currentweight = weight[left] + weight[right]
        if currentweight > x:
            right -= 1
            currentweight -= weight[right]
        else:
            count -= 1
            left += 1
            right -= 1
            currentweight = 0
    return count

if __name__ == '__main__':
    n, x = map(int, input().split())
    weight = list(map(int, input().split()))
    print(solve(weight, x))