c = []
for i in range(3):
    c.append(list(map(int, input().split())))
a = [0,0,0]
b = [0,0,0]
for i in range(3):
    b[i] = c[i][0] - 0
for i in range(3):
    a[i] = c[0][i] - b[0]
for i in range(3):
    for j in range(3):
        if a[j] + b[i] != c[i][j]:
            print("No")
            exit()
print("Yes")