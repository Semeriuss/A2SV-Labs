def solve(arrivalTimes, buses, limit):
    arrivalTimes.sort()
    res = 0
    limit = len(arrivalTimes)//buses
    for i in range(0, len(arrivalTimes), limit):
        res = max(res, arrivalTimes[i + limit - 1] - arrivalTimes[i])
    return res


# if __name__ == "__main__":
#     N, M, C = map(int, input().split())
#     cows = list(map(int, input().split()))
#     ret = solve(cows, M, C)
#     print(ret)

if __name__ == "__main__":
    fin = open ('convention.in', 'r')
    fout = open ('convention.out', 'w')
    N, M, C = list(map(int, fin.readline().split()))
    cows = list(map(int, fin.readline().split()))
    ret = solve(cows, M, C)
    fout.write (str(ret) + '\n')
    fout.close()
