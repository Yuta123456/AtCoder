sx,sy,tx,ty = list(map(int, input().split()))
ans = []
#一回目
for i in range(ty - sy):
    ans.append("U")
for i in range(tx - sx):
    ans.append("R")
for i in range(ty - sy):
    ans.append("D")
for i in range(tx - sx):
    ans.append("L")
#二回目
ans.append("L")
for i in range(ty + 1 - sy):
    ans.append("U")
for i in range(tx + 1 - sx):
    ans.append("R")
ans.append("D")
ans.append("R")
for i in range(ty + 1 - sy):
    ans.append("D")
for i in range(tx + 1 - sx):
    ans.append("L")
ans.append("U")
print("".join(ans))