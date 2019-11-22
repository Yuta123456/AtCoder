
x, y, z, k = map(int,input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
Z = list(map(int, input().split()))
mul_x_y = []
for i in X:
    for j in Y:
        mul_x_y.append(i+j)
mul_x_y.sort()
mul_x_y.reverse()
Z.sort()
Z.reverse()
mul_x_y = mul_x_y[:k]
Z = Z[:k]
ans = []
for i in mul_x_y:
    for j in Z:
        ans.append(i + j)
ans.sort()
ans.reverse()
for i in range(k):
    print(ans[i])