n = int(input())
s, t  = input().split()
ans = ""
for i in range(2*n):
    if i % 2 == 0:
        ans += s[i//2]
    else:
        ans += t[i//2]
print(ans)