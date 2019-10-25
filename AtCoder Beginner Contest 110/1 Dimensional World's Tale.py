n,m,s,t = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
if x[n - 1] <= y[0] and x[n - 1] <= t and y[0] >= s:
    print("No War")
else:
    print("War")
