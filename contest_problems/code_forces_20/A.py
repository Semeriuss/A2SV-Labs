def solve(k, s):
    counter = [0 for i in range(26)]
    res = ["a" for _ in range(k)]
    for c in s:
        counter[ord(c) - ord('a')] += 1
    
    charCount = 0
    for j in range(k):
        ct = 0
        while (ct < n/k and counter[ct] > 0):
            counter[ct] -= 1
            ct += 1
        res[j] = chr(ord('a') + ct )

    return "".join(res)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        s = input()
        print(solve(k, s))