def euqlid(a,b):
    if a < b :
        tmp = a
        a = b
        b = tmp

    while b != 0:
        rem = a % b
        a = b
        b = rem

    return a
N,X = list(map(int, input().split()))
x = list(map(int, input().split()))
x.append(X)
x.sort()
l = []
for i in range(N):
    l.append(x[i + 1] - x[i])
if len(l)  == 1:
    print(l[0])
    exit()
else:
    ans = euqlid(l[0],l[1])

for i in range(2,N - 1):
    ans = euqlid(ans,l[i])
print(ans)
