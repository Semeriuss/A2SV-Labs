def solve(nums):
    return len(set(nums))

if __name__ == '__main__':
    n, nums = int(input()), list(map(int, input().split()))
    print(solve(nums))