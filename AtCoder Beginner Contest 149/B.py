a,b,k = map(int, input().split())
if a > k:
    print("{} {}".format(a-k, b))
else:
    print("{} {}".format(0, max(0, b - (k - a))))