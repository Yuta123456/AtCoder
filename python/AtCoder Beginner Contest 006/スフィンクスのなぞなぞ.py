n, m = map(int, input().split())
ans = [2 for i in range(n)]
if 2*n <= m <= 4*n:
    for i in range(2*n, m):
        ans[i%n] += 1
    print("{} {} {}".format(ans.count(2),ans.count(3),ans.count(4)))
else:
    print("{} {} {}".format(-1,-1,-1))