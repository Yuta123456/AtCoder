n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
div = set()
for i in range(n):
    flag = True
    for j in range(1,int(pow(a[i], 0.5)) + 1):
        if a[i] % j == 0:
            if j in div or a[i] // j in div:
                flag = False
                break
    div.add(a[i])
    if flag:
        if i != n-1 and a[i] != a[i+1]:
            ans += 1
        if i == n-1:
            ans += 1
print(ans)
