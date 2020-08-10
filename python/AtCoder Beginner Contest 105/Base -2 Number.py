n = int(input())
ans = ''
i = 0
if n == 0:
    print(0)
    exit()
while n != 0:
    if n % ((-2) ** (i + 1)) == 0:
        ans = '0' + ans
    else:
        ans = '1' + ans
        n -= (-2) ** i
    i += 1
print(ans)
