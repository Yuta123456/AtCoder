import sys
sys.setrecursionlimit(10**6)
n = int(input())
adjacent_list = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
finished = set()
inf = 10**9
dist = [inf for i in range(n+1)]
def dfs(node):
    finished.add(node)
    for i in adjacent_list[node]:
        if i not in finished:
            dist[i] = dist[node]+1
            dfs(i)
dist[1] = 0
rem_1 = [i+1 for i in range(n) if (i+1) % 3 == 1]
rem_2 = [i+1 for i in range(n) if (i+1) % 3 == 2]
rem_0 = [i+1 for i in range(n) if (i+1) % 3 == 0]
index_0 = 0
index_1 = 0
index_2 = 0
dfs(1)
ans = []
count_even = 0
count_odd = 0
for i in range(1,len(dist)):
    if dist[i] % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

#場合分け
if count_even > n/3 and count_odd > n/3:
    #この場合、普通にやる
    for i in range(1,len(dist)):
        if dist[i] % 2 == 1:
            if index_2 < len(rem_2):
                ans.append(rem_2[index_2])
                index_2 += 1
            else:
                ans.append(rem_0[index_0])
                index_0 += 1
        else:
            if index_1 < len(rem_1):
                ans.append(rem_1[index_1])
                index_1 += 1
            else:
                ans.append(rem_0[index_0])
                index_0 += 1
elif count_even <= n/3:
    #1からの距離が偶数のところが全体の1/3を閉めない場合
    #そこに全部3の倍数を入れてしまえば、題意を満たす
    li = rem_1 + rem_2
    index = 0
    for i in range(1,len(dist)):
        if dist[i] % 2 == 0:
            ans.append(rem_0[index_0])
            index_0 += 1
        else:
            if index < len(li):
                ans.append(li[index])
                index += 1
            else:
                ans.append(rem_0[index_0])
                index_0 += 1
else:
    ##1からの距離が奇数のところが全体の1/3を閉めない場合
    #そこに全部3の倍数を入れてしまえば、題意を満たす
    li = rem_1 + rem_2
    index = 0
    for i in range(1,len(dist)):
        if dist[i] % 2 == 1:
            ans.append(rem_0[index_0])
            index_0 += 1
        else:
            if index < len(li):
                ans.append(li[index])
                index += 1
            else:
                ans.append(rem_0[index_0])
                index_0 += 1
for i in ans:
    print(i, end=" ")

