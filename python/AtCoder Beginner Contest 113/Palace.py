n = int(input())
t, a = list(map(int, input().split()))
h = list(map(int, input().split()))
min = abs(a - (t - h[0] * 0.006))
minIndex = 0
for i in range(n):
    if min > abs(a - (t - h[i] * 0.006)):
        min = abs(a - (t - h[i] * 0.006))
        minIndex = i
print(minIndex + 1)
