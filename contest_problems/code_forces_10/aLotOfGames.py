def aLotOfGames(k):
    return "First" if k%2 != 0 else "Second"

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    for i in range(n):
        input()
    print(aLotOfGames(k))