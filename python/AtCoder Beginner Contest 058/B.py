o = input()
e = input()
ans = ""
for i in range(len(o) + len(e)):
    if i % 2 == 0:
        ans += o[i//2]
    else:
        ans += e[i//2]
print(ans)