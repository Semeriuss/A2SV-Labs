N, D = map(int, input().split())
candidates = sorted(map(int, input().split()))
res = 0
i, j = 0, N - 1
while i <= j and j >= 0:
    if candidates[j] > D:
        res += 1
        j -= 1
    else:
        rem = D // candidates[j]
        if i + rem <= j:
            i += rem
            j -= 1
            res += 1
        else:
            break
print(res)
