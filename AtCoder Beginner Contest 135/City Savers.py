n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count  = 0
for i in range(n):
    if(b[i] <= a[i]):
        a[i] -= b[i]
        count += b[i]
    else:
        sub = b[i] - a[i]
        if sub < a[i + 1]:
            a[i + 1] -= sub
            count += (a[i] + sub)
            a[i] = 0
        else:
            count += a[i] + a[i + 1]
            a[i + 1] = 0
            a[i] = 0
print(count)
