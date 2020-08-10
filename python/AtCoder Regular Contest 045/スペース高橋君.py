s = input().split()
ans = ""
for i in range(len(s)):
    if s[i] == "Left":
        ans += "< "
    elif s[i] == "Right":
        ans += "> "
    else:
        ans += "A "
print(ans[:-1])
