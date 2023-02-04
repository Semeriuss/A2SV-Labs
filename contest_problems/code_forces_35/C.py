from bisect import bisect_right

shops = int(input())
prices = sorted(map(int, input().split()))
q = int(input())
queries = [int(input()) for _ in range(q)]

for query in queries:
    print(max(0, bisect_right(prices, query)))

