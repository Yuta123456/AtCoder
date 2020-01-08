n = int(input())
adjacent_list = [[]for i in range(n+1)]
for i in range(n-1):
    a,b = map(int ,input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
c = list(map(int, input().split()))
c.sort(reverse=True)
adjacent_list.sort(key = lambda x:len(x),reverse=True)
ans = 0
for i in range(n):
    ans += len(adjacent_list[i]) * c[i]
print(ans)