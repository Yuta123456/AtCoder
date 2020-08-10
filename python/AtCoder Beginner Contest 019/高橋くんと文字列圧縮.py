s = input()
pre = 0
k = []
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        k.append(s[pre:i])
        pre = i
k.append(s[pre:])
ans = ""
for i in range(len(k)):
    ans += k[i][0]+str(len(k[i]))
print(ans)