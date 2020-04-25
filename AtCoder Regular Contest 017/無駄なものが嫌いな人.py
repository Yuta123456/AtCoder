import sys
sys.setrecursionlimit(10**9)
n, x = map(int, input().split())
weight = []
ans = 0
for i in range(n):
    weight.append(int(input()))
weight.sort()
latter = dict()
former = dict()
def dfs(cur_sum, index_s, index_l,dictionary):
    if cur_sum in dictionary:   
        dictionary[cur_sum] += 1
    else:
        dictionary[cur_sum] = 1
    if cur_sum > x:
        return
    for i in range(index_s+1,index_l):
        dfs(cur_sum + weight[i], i,index_l, dictionary)
dfs(0,-1,n//2,former)
dfs(0,n//2 - 1,n,latter)
for i in former.keys():
    key = x - i
    if key in latter:
        ans += former[i] * latter[key]
print(ans)