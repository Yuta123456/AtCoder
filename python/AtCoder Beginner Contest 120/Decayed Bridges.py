n, m = map(int, input().split())
data = []
for i in range(m):
    data.append(list(map(int, input().split())))
data.reverse()
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
    def printsize(self):
        print(self.size)
    def printparents(self):
        print(self.par)
ans = []
ans.append(n*(n-1)//2)
graph = UnionFind(n)
for i in range(1, len(data)):
    a, b = data[i - 1]
    #print("{} {}".format(a, b))
    if graph.same_check(a,b):
        ans.append(ans[i-1])
    else:
        ans.append(ans[i-1] - (graph.getsize(a) * graph.getsize(b)))
        graph.union(a,b)
ans.reverse()
for i in ans:
    print(i)


