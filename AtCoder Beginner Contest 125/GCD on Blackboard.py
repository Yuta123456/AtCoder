def euclid(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    while x % y != 0:
        temp = x
        x = y
        y = temp % y
    return y

n = int(input())
data = list(map(int, input().split()))
array = data
L = []
L.append(0)
R = []
R.append(0)
m = []
for i in range(n):
    L.append(euclid(L[i], data[i]))
data.reverse()
for i in range(n):
    R.append(euclid(R[i], data[i]))
R.reverse()
for i in range(0,n):
    m.append(euclid(L[i] , R[i + 1]))
print(max(m))
