n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))
ans = ""
for i in range((n+1)//2):
    formar = set()
    latter = set()
    for j in range(n):
        formar.add(grid[i][j])
        latter.add(grid[n-i-1][j])
    if len(formar & latter) == 0:
        print(-1)
        exit()
    else:
        ans += list(formar & latter)[0]
if n % 2 == 0:
    print(ans + "".join(map(str,reversed(list(ans)))))
else:
    print(ans[:-1] + "".join(map(str,reversed(list(ans)))))