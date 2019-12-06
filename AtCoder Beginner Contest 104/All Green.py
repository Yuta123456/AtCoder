import math
d,g = map(int, input().split())
data = []
for i in range(1,d+1):
    data.append([100*i, *list(map(int, input().split()))])
print(data)
data.reverse()
ans = 0
total = 0
for i in data:
    point, count, bonus = i
    if total + (point * count + bonus) < g:
        total += point * count + bonus
        ans += count
    elif total + (point * count + bonus) == g:
        ans += count
        print(ans)
        exit()
    else:
        ans += math.ceil((g - total) / point)
        print(ans)
        exit()