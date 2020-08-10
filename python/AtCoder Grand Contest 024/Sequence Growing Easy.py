
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
    if i == 0:
        if a[0] != 0:
            print("-1")
            exit()
    else:
        if a[i] >= a[i-1]+2:
            print("-1")
            exit()
a += [a[-1]]
a.reverse()

ans = 0
for i in range(1,n):
    if a[i] >= a[i-1]:
        ans += a[i]
print(ans)



