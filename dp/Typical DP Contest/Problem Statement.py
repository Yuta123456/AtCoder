n = int(input())
data = list(map(int,input().split()))
ans = set()
ans.add(0)
for i in range(n):
    for j in list(ans):
        ans.add(j + data[i])
print(len(ans))
