n, t = map(int, input().split())
homework = []
for i in range(n):
    homework.append(list(map(int, input().split())))
homework.sort(key=lambda x: x[1] - x[0])
serious = sum([homework[i][0] for i in range(n)])
not_serious = 0
#境界を探す
for i in range(n+1):
    if serious + not_serious <= t:
        print(i)
        exit()
    elif i == n:
        print(-1)
        exit()
    else:
        serious -= homework[i][0]
        not_serious += homework[i][1]