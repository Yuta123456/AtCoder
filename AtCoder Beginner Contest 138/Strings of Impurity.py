s = input()
t = input()
data = {}
max = len(s)
for i in range(24):
    data[chr(i + ord('a'))] = max + 1
for i in range(len(s)):
    if data[s[i]] > i + 1:
        data[s[i]] = i + 1
ans = 0
pre = max
for i in range(len(t)):
    if data[t[i]] == max + 1:
        print(-1)
        exit()
    else:
        if pre < data[t[i]]:
            ans += (data[t[i]] - pre)
            pre = data[t[i]]
        else:
            ans += (max + data[t[i]] - pre)
            pre = data[t[i]]
    
print(ans)
