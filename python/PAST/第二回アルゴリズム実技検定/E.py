n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    count = 1
    k = a[i]-1
    while k != i:
        k = a[k] - 1
        count += 1
    print(count, end=" ")
