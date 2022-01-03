def stableArrangement(n, k):
    if n == k == 1: 
        return "R"

    if k >= n:
        return -1

    res = ["R" + "." * (n - 1)]
    nextPos = 2

    rank = "." * n
    
    remRooks = k - 1
    remRanks = n - 1
    while remRanks > 0:
        res.append(rank)
        remRanks -= 1
        if remRooks > 0:
            nextRank = "." * nextPos + "R" + "." * (n - nextPos - 1)
            remRooks -= 1
            if remRanks > 0:
                res.append(nextRank)
                remRanks -= 1
                nextPos += 2
            else:
                break
            if remRooks > 0 and nextPos >= n: break
            
    
    if remRooks > 0: return -1
    return res

    

    



if __name__ == "__main__":
    t = int(input())
    ans = []
    for _ in range(t):
        n, k = map(int, input().split())
        ans.append(stableArrangement(n, k))

    for res in ans:
        if res == -1:
            print(-1)
        else:
            for rank in res:
                print(rank)