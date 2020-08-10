n = int(input())
a = list(map(int, input().split()))
a = [0] + a
cur_max = 0
ans = 0
for i in range(n+1):
    if a[i] > cur_max:
        ans += 1
        cur_max = a[i]
print(ans)