def solve(k, s):
    counter = [0 for i in range(26)]
    res = []
    for c in s:
        counter[ord(c) - ord('a')] += 1
    
    charCount = 0
    for i, count in enumerate(counter):
        net = count - k
        print(chr(ord('a') + i) + " " + str(count) + " " + str(k) + " " + str(net) + " " + str(res))
        if charCount >= k:
                break
        if net < 0:
            factor = (min(abs(net), k - charCount))
            res.append(chr(ord('a') + i) * factor)
            charCount += factor

    if charCount < k:
        res.append(chr(ord(res[-1]) + 1))

    return "".join(res[::-1])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        s = input()
        print(solve(k, s))