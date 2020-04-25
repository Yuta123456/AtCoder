n = int(input())
b = list(map(int, input().split()))
ans = []
index = 0
count = 0
while count <= 10000 and len(b) > 0:
    index = len(b) - 1
    while index >= 0:
        if index + 1 == b[index]:
            ans.append(b[index])
            del b[index]
            index = len(b) - 1
            continue
        index -= 1
        count += 1
if len(ans) == n:
    ans.reverse()
    for i in range(n):
        print(ans[i])
else:
    print(-1)