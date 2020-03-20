import bisect
s = input()
t = input()
data = {}
max_s = len(s) + 1
for i in range(26):
    data[chr(i + ord('a'))] = []
for i in range(len(s)):
    data[s[i]].append(i+1)
for i in range(26):
    data[chr(i + ord('a'))].append(max_s)
pre = 0
ans = 0
for i in range(len(t)):
    char = t[i]
    if len(data[char]) == 1:
        print(-1)
        exit()
    else:
        index = bisect.bisect_left(data[char], pre+1)
        if data[char][index] == max_s:
            ans += len(s) - pre
            pre = data[char][0]
            ans += pre
        else:
            ans += data[char][index] - pre
            pre = data[char][index]
print(ans)
