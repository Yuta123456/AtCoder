n = int(input())
s = input()
ans = 500
def dfs(st, cnt):
    if st == s:
        global ans
        ans = min(cnt, ans)
        return 
    if len(st) <= n:
        if cnt % 3 == 0:
            dfs('b' + st + 'b', cnt + 1)
        elif cnt % 3 == 1:
            dfs('a' + st + 'c', cnt + 1)
        else:
            dfs('c' + st + 'a', cnt + 1)
dfs('b', 1)
if ans == 500:
    print(-1)
else:
    print(ans -1)