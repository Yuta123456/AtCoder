import sys
sys.setrecursionlimit(10**6)
n = int(input())
mod = 10**9+7
adjacent_list = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
memo = dict()
def dfs(node, pre_node,is_black):
    if (node,is_black) in memo:
        return memo[(node,is_black)]
    if is_black:
        tmp = 1
        for i in adjacent_list[node]:
            if i != pre_node:
                #今回は黒確定
                #つまり、次は白
                tmp *= dfs(i,node,False)
            tmp %= mod
        memo[(node,is_black)] = tmp
        return tmp
    else:
        tmp = 1
        #今回は白確定
        for i in adjacent_list[node]:
            if i != pre_node:
                tmp *= dfs(i,node,False) + dfs(i,node,True)
            tmp %= mod
        memo[(node,is_black)] = tmp
        return tmp
print((dfs(1,0,True) + dfs(1,0,False)) % mod)




