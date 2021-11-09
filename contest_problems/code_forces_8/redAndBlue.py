def maxSubArraySum(red, blue):

    prefixRed = [red[0]]
    prefixBlue = [blue[0]]

    maxRed = max(0, prefixRed[-1])
    for i in range(1, len(red)):
        prefixRed.append(prefixRed[-1] + red[i])
        maxRed = max(maxRed, prefixRed[-1])
    
    maxBlue = max(0, prefixBlue[-1])
    for j in range(1, len(blue)):
        prefixBlue.append(prefixBlue[-1] + blue[j])
        maxBlue = max(maxBlue, prefixBlue[-1]) 

    return maxBlue + maxRed

if __name__ == "__main__":
    t = int(input())

    tests = []
    res = []
    for i in range(t):
        n = int(input())
        red = list(map(int, input().split()))

        m = int(input())
        blue = list(map(int, input().split()))
        res.append(maxSubArraySum(red, blue))

    print(*res, sep="\n")
