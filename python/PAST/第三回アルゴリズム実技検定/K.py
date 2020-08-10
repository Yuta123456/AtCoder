import sys
sys.setrecursionlimit(10**7)
n, q = map(int, input().split())
#table[i][0] -> end
table = [i for i in range(n+1)]
#node[i] := iの親と、子を保存
#node[i][0] = 親
#node[i][1] = 子
node = [[None, None] for i in range(n+1)]
for i in range(n+1):
    node[i][0] = i + (n + 1)
for i in range(q):
    f, t, x = map(int, input().split())
    from_end = table[f]
    if node[x][0] == f + (n+1):
        table[f] = f + n + 1
    else:
        table[f] = node[x][0]
    node[x][0] = table[t]
    if table[t] < n:
        node[table[t]][1] = x
    table[t] = from_end
ans = [-1 for i in range(n+1)]
def check(point):
    if ans[point] != -1:
        return ans[point]
    if node[point][0] > n:
        ans[point] = node[point][0] - (n + 1)
        return ans[point]
    else:
        ans[point] = check(node[point][0])
        return ans[point]
for i in range(1,n+1):
    if ans[i] != -1:
        print(ans[i])
    else:
        check(i)
        print(ans[i])