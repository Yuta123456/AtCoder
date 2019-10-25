n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = list(str(format(k, 'b')))
L = len(ans)
zero = 0
one = 0
for i in range(n):
    a[i] = str(format(a[i], 'b'))
    if len(a[i]) < L:
        a[i] = '0' * (L - len(a[i])) + a[i]
for i in range(L):
    one = 0
    zero = 0
    for j in range(n):
        if a[j][i] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        ans[i] = '1'
    else:
        ans[i] = '0'
ans = "".join(ans)
sum = 0
for i in range(n):
    a[i] = int(a[i], 2)
    sum += a[i] ^ int(ans, 2)
print(sum)
