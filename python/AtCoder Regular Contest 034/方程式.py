n = int(input())
ans = []
for i in range(max(1, n - 180), n):
    k = i
    for j in str(i):
        k += int(j)
    if k == n:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])