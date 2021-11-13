from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    qualifications = list(map(int, input().split()))
    m = int(input())

    costs = defaultdict(lambda: float("inf"))
    for _ in range(m):
        supervisor, subordinate, cost = map(int, input().split())
        costs[subordinate] = min(costs[subordinate], cost)

    ret = sum(costs.values()) if len(costs) == n - 1 else -1
    print(ret)
  
