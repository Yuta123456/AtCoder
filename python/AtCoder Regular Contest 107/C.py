n, k = map(int, input().split())
a = []
mod = 998244353
for i in range(n):
    a.append(list(map(int, input().split())))
row = [[] for i in range(n+1)]
column = [[] for i in range(n+1)]
for i in range(n):
    #jからiに通るか？
    for j in range(i+1, n):
        flag = True 
        for p in range(n):
            if a[i][p] + a[j][p] > k:
                flag = False
                break
        if flag:
            row[i].append(j)
            row[j].append(i)
for i in range(n):
    #jからiに通るか？
    for j in range(i+1, n):
        flag = True 
        for p in range(n):
            if a[p][i] + a[p][j] > k:
                flag = False
                break
        if flag:
            column[i].append(j)
            column[j].append(i)
finished = set()
fact = [0 for i in range(100)]
fact[0] = 1
for i in range(1,100):
    fact[i] = (fact[i-1] * i) % mod



def dfs(node, array):
    finished.add(node)
    for i in array[node]:
        if i not in finished:
            dfs(i, array)
r = 1
searched = set()
for i in range(n):
    if i in searched:
        continue
    finished = set()
    dfs(i, row)
    r *= fact[len(finished)]
    r %= mod
    searched |= finished

c = 1
searched = set()
for i in range(n):
    if i in searched:
        continue
    finished = set()
    dfs(i, column)
    c *= fact[len(finished)]
    c %= mod
    searched |= finished
print(r * c % mod)