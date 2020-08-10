n = int(input())
s = input()
pre = s[0]
ans = 1
for i in range(1, n):
    if pre != s[i]:
        pre = s[i]
        ans += 1
print(ans)
