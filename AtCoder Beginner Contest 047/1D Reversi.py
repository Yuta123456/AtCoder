s = list(input())
pre = s[0]
count = 0
for i in range(1,len(s)):
    if pre != s[i]:
        count += 1
    pre = s[i]
print(count)