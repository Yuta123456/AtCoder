n, l = list(map(int ,input().split()))
sumApple = sum(range(l,l+n))
aMin = 10000
for i in range(1,n + 1):
    if abs(l + i - 1) < abs(aMin):
        aMin = (l + i - 1)
print(sumApple - aMin)
