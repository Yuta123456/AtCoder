n , q = list(map(int, input().split()))
s = input()
data = []
for i in range(q):
    data.append(list(map(int, input().split())))
ans = [0 for i in range(n)]
count = 0
for i in range(1,n):
    if s[i - 1] == 'A' and s[i] == 'C':
        count += 1
    ans[i] = count
for i in range(q):
    l = data[i][0]
    r = data[i][1]
    print(ans[r - 1] - ans[l - 1])
