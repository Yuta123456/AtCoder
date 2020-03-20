s = list(input())
k = int(input())
ans = 0
for i in range(1,len(s)-1):
    if s[i] == s[i+1]:
        ans += 1
        s[i+1] = '_'
if s[0] == s[-1]:
    ans += 1
ans *= k
print(ans)