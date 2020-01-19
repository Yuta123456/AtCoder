n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
odd = []
even = []

for i in range(n):
    if i % 2 == 0:
        even.append(a[i])
        odd.append(b[i])
    else:
        even.append(b[i])
        odd.append(a[i])
#odd, evenの二部グラフで、自身に辺を通さない
#a[i] <=  b[j]の時辺を通す 
graph = [[] for i in range(n*2)]
for i in range(n):
    for j in range(n, n*2):
        if i != j % n and even[i] <= odd[j%n]:
            graph[i].append(j)

for i in range(n,n*2):
    for j in range(n):
        if  j != i % n and odd[i % n] <= even[j]:
            graph[i].append(j)
#グラフで一筆書きをする。パスがnになったら終わり。その順番を実現するために考える
def clear_maze(start, finished, path):
    f = finished | set([start%n])
    path = path + [start]
    if len(path) == n:
        check(path)
    else:
        for i in graph[start]:
            if (i % n not in f):
                clear_maze(i, f, path)
def check(path):
    #この順番に並ぶための最小
    print(path)
    array = [i % n for i in path]
    cand = 0
    global ans
    for i in range(1,n,1):
        for j in range(i,n,1):
            if array[i-1] > array[j]:
                cand += 1
    ans = min(cand, ans)
inf = 18**2
ans = inf
for i in range(n):
    #iから始める迷路を解く
    clear_maze(i, set(), [])
if ans == inf:
    print(-1)
else:
    print(ans)


