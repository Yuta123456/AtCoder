n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
ans = []
flag = False
for i in range(len(a) - 1):
    if flag == 1:
        flag = -1
        continue
    if a[i] == a[i+1]:
        ans.append(a[i])
        if flag == -1:
            break
        flag = 1
if len(ans) == 2:
    print(ans[0] * ans[1])
else:
    print(0)