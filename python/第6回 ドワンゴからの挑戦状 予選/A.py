n = int(input())
data = []
for i in range(n):
    s, t = input().split()
    data.append([s, int(t)])
x = input()
ans = 0
flag = False
for i in range(n):
    if flag:
        ans += data[i][1]
    if x == data[i][0]:
        flag = True
print(ans)