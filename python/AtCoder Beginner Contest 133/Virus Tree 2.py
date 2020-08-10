import sys
sys.setrecursionlimit(10**5)
n, k = map(int, input().split())
mod = 10 ** 9 + 7
adjacent_list = [[] for i in range(n+1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
finished = set([1])
ans = k
def dfs(current, finished,num):
    global ans
    global k
    unsearched = set(adjacent_list[current]) - finished
    num = max(k - 1, num)
    if len(unsearched) == 0:
        return
    for i in unsearched:
        finished.add(i)
        num -= 1
        ans *= num
        ans %= mod
        dfs(i,finished, num)
dfs(1,finished,k)
print(ans)