n,x,y = map(int, input().split())
x -= 1
y -= 1
ans = [0 for i in range(n+1)]
for i in range(0,n):
    for j in range(i+1,n):
        if (i <= x and j <= x) or (i >= y and j >= y):
            ans[j-i] += 1
        else:
            k = min(abs(x-i) + 1 + abs(y-j), j-i)
            ans[k] += 1
for i in range(1,n):
    print(ans[i])
