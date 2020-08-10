n,m,s,t = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
for i in range(-101,101):
    if x[-1] < i <= y[0] and s < i <= t:
        print("No War")
        exit()
print("War")
