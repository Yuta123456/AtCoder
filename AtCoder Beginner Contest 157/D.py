import sys
input = sys.stdin.readline
n,m,k = map(int, input().split())
class UnionFind:
    def __init__(self, n):
        #親ノードの番号を格納
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)
    def find(self, x):
        #根ならその番号を返す
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def same_check(self, x, y):
        #同じかどうかの確認
        return self.find(x) == self.find(y)
    def union(self, x, y):
        #統合する
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
            self.size[x] = 0
        elif self.rank[x] > self.rank[y]:
            self.par[y] = x
            self.size[x] += self.size[y]
            self.size[y] = 0
        else:
            self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]
            self.size[y] = 0
    def getsize(self, x):
        p = self.find(x)
        return self.size[p]
u = UnionFind(n)
ans_li = [-1 for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    u.union(a,b)
    ans_li[a] -= 1
    ans_li[b] -= 1
for i in range(k):
    a,b = map(int, input().split())
    if u.find(a) == u.find(b):
        ans_li[a] -= 1
        ans_li[b] -= 1
for i in range(1,n+1):
    ans_li[i] += u.getsize(i)
    print(ans_li[i], end = " ")

