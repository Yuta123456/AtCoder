n,c = map(int, input().split())
a = list(map(int, input().split()))
ans = [0 for i in range(n+1)]
pre_index = [0 for i in range(c+1)]
for i in range(n):
    index = pre_index[a[i]]
    left = (i - index) + 1
    right = (n - i)
    ans[a[i]] += left * right
    pre_index[a[i]] = i + 1
for i in range(1,c+1):
    print(ans[i])