n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1,len(a)):
    height_step = a[i] - a[i-1]
    if height_step < 0:
        ans -= height_step
        a[i] = a[i-1]
print(ans)