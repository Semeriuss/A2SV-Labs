def solve(weight, x):
    weight.sort()
    count = 1
    left, right = 0, len(weight) - 1
    while left < right:
        currentweight = weight[left] + weight[right]
        if currentweight > x:
            count += 1
            right -= 1
            currentweight -= weight[right]
        elif currentweight < x:
            while currentweight < x and left + 1 < right:
                left += 1
                currentweight += weight[left]
            currentweight = weight[left] + weight[right]


    

if __name__ == '__main__':
    n, x , weight = int(input()), int(input()), list(map(int, input().split()))
    print(solve(weight))