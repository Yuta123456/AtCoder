from collections import deque
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
adjacent_list = [[] for i in range(n+1)]
not_root = set()
for i in range(m):
    x, y = map(int, input().split())
    not_root.add(y)
    adjacent_list[x].append(y)
root_cand = set(list(range(1, n+1))) - not_root
root_cand = deque(root_cand)
dp = [-1] * (n+1)
def dfs(node):
    if len(adjacent_list[node]) == 0:
        dp[node] = 0
        return dp[node]
    elif dp[node]  != -1:
        return dp[node]

    for i in adjacent_list[node]:
        dp[node] = max(dp[node], dfs(i) + 1)
    return dp[node]
n = len(root_cand)
while n != 0:
    root = root_cand.pop()
    n -= 1
    dfs(root)
print(max(dp))
