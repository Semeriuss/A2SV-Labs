n = int(input())
valya = input()
tolya = input()

class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
    
    def find(self, u):
        if u != self.root[u]:
            self.root[u] = self.find(self.root[u])
        return self.root[u]
    
    def union(self, u, v):
        x, y = self.find(u), self.find(v)
        if x != y:
            self.root[y] = self.root[x]
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

res = []
uf = UnionFind(26)
for i in range(n):
    if valya[i] == tolya[i]:
        continue 
    vNum = ord(valya[i]) - ord('a')
    tNum = ord(tolya[i]) - ord('a')
    if uf.connected(vNum, tNum):
        continue 
    uf.union(vNum, tNum)
    res.append(valya[i] + " " + tolya[i])
    
print(len(res))
for spell in res:
    print(spell)
