n ,m = list(map(int, input().split()))
q = []
for i in range(m):
    q.append(list(map(int, input().split())))
q.sort(key=lambda x: x[1])
ans = 0
last_cut_bridge = -1
for i in range(m):
    a,b = q[i]
    if a <= last_cut_bridge <= b:
        continue
    else:
        last_cut_bridge = b-1
        ans += 1
print(ans)