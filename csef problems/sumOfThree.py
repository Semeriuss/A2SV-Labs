def solve(nums, x):
    for i, num in enumerate(nums):
        hashmap = {}
        res = [-1, -1]
        for j, num2 in enumerate(nums):
            if num2 in hashmap and i != j and hashmap[num2] != i:
                res = [hashmap[num2] + 1, j + 1]
                break
            hashmap[x - num2 - num] = j
        if res != [-1, -1]:
            x, y = res[0], res[1]
            return f'{i + 1} {x} {y}'
    return 'IMPOSSIBLE'
    

if __name__ == '__main__':
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(nums, x))