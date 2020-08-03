n,m,q = map(int, input().split())
adjacent_list = [[] for i in range(n+1)]
for i in range(m):
    a, b =  map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
color = [-1] + list(map(int, input().split()))
for _ in range(q):
    s = list(map(int, input().split()))
    print(color[int(s[1])])
    if s[0] == 1:
        for i in adjacent_list[int(s[1])]:
            color[i] = color[int(s[1])]
    else:
        color[int(s[1])] = int(s[2])
