n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
total = 0
for i in range(n + 2):
    total += abs(a[i] - a[i - 1])
for i in range(1,n+1):
    k = abs(a[i] - a[i-1]) + abs(a[i+1] - a[i])
    print(total - k + abs(a[i+1] - a[i-1]))
