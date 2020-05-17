n = int(input())
c = list(map(int, input().split()))
q = int(input())
all_min = min(c)
odd_min = min(c[::2])
odd_count = (len(c) + 1) // 2
all_sell = 0
odd_sell = 0
ans = 0
for i in range(q):
    s = input()
    if s[0] == "1":
        d,x,a = map(int, s.split())
        x -= 1
        #odd
        if x % 2 == 0:
            if c[x] - a - all_sell - odd_sell >= 0:
                c[x] -= a
                ans += a
                odd_min = min(odd_min, c[x])
                all_min = min(all_min, c[x])
        else:
            if c[x] - a - all_sell >= 0:
                c[x] -= a
                ans += a
                all_min = min(all_min, c[x])
    elif s[0] == "2":
        d,a = map(int, s.split())
        if odd_min - a >= 0:
            odd_min -= a
            ans += odd_count * a
            odd_sell += a
            all_min = min(all_min, odd_min)
    else:
        d,a = map(int, s.split())
        if all_min - a >= 0:
            ans += len(c) * a
            all_min -= a
            odd_min -= a
            all_sell += a
print(ans)