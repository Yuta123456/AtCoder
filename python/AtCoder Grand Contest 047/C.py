n = int(input())
a = list(map(int, input().split()))
a.sort()
P = 200003
ans = 0
count = 0
sum_array = 0
for i in range(n):
    sum_array += a[i]
    if sum_array > P:
        count += 1
        sum_array %= P
for i in range(n):
    k = sum_array - a[i]
    c = count
    if k < 0:
        c -= 1
        k += P
    ans += P * c + a[i] * k
print(ans // 2)
