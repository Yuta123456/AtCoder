import sys
sys.setrecursionlimit(10**7)
n = int(input())
adjacent_list = [[] for i in range(n+1)]
for i in range(2,n+1):
    s = int(input())
    adjacent_list[s].append(i)
def count_node(node):
    res = 1
    for i in adjacent_list[node]:
        res += count_node(i)
    return res
ans = 0
for i in adjacent_list[1]:
    ans = max(ans, count_node(i))
print(ans + ad)


