s = input()
ans = ""
for i in s:
    if ord(i) < 58:
        ans += i
print(ans)