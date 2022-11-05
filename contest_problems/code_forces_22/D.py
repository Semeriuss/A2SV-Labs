from collections import Counter
def solve(a):
    freq = Counter(list(d%10 for d in a))
    for i in range(10):
        if freq[i] == 0: continue 
        freq[i] -= 1
        for j in range(10):
            if freq[j] == 0: continue 
            freq[j] -= 1
            for num in [3, 13, 23]:
                if freq[num - (i + j)]:
                    return "YES"
            freq[j] += 1
        freq[i] += 1
            
    return "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))