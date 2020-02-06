n, x = map(int, input().split())
a = list(map(int, input().split()))
bit = list(format(x, 'b'))

ans = 0
bit.reverse()
for i in range(len(bit)):
    if bit[i] == '1':
        ans += a[i]
print(ans)