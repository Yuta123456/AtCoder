n, m = map(int, input().split())
ans = ["-1" for i in range(n)]
for i in range(m):
    s, c = input().split()
    s = int(s)
    if s == 1 and c == '0' and n != 1:
        print(-1)
        exit()
    if ans[s-1] == "-1":
        ans[s-1] = c
    else:
        if ans[s-1] != c:
            print(-1)
            exit()
if ans[0] == '-1':
    ans[0] = "1"
if m == 0:
    ans[n-1] = "0"
print(("".join(ans)).replace("-1","0"))
