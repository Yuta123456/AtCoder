s = input()
a = list(map(int, input().split()))
ans = ""
for i in range(len(s) + 1):
    for j in range(4):
        if i  == a[j]:
            ans += '"'
    if i < len(s):
        ans += s[i]
print(ans)