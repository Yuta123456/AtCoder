import sys 
input = sys.stdin.readline
n = int(input())
data = []
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
x = []
y = []
for i in range(n):
    a,b = map(int, input().split())
    x.append([a,i+1])
    y.append([b,i+1])
x.sort(key = lambda x: x[0])
y.sort(key = lambda x: x[0])
edge = []
for i in range(n-1):
    edge.append([x[i+1][0] - x[i][0],x[i+1][1],x[i][1]])
    edge.append([y[i+1][0] - y[i][0],y[i+1][1],y[i][1]])
#edge[i][0] = cost, [1] -> [2]でつながっている辺
edge.sort(key = lambda x: x[0])
UF = UnionFind(n)
ans = 0
for i in range(len(edge)):
    cost,a,b = edge[i]
    if UF.same_check(a,b):
        continue
    else:
        ans += cost
        UF.union(a,b)
print(ans)



