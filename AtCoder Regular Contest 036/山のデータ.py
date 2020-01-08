n = int(input())
h = []
ans = 0

for i in range(n):
    h.append(int(input()))
increase = [0 for i in range(n)]
decrease = [0 for i in range(n)]
inc_count = 1
for i in range(n-1):
    increase[i] = inc_count
    if h[i] >= h[i+1]:
        inc_count = 0
    inc_count += 1
increase[-1] = inc_count

inc_count = 1
h.reverse()
for i in range(n-1):
    decrease[i] = inc_count
    if h[i] >= h[i+1]:
        inc_count = 0
    inc_count += 1
decrease[-1] = inc_count
decrease.reverse()
for i in range(n):
    ans = max(ans, increase[i] + decrease[i] - 1)
print(ans)
