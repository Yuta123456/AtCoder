n,m = map(int, input().split())
for i in range(m):
    print("{} {}".format(i+1, n-i))
    if i+1 == n-1:
        break
