x, y = map(int, input().split())
for i in range(101):
    for j in range(101):
        if i + j == x and i * 2 + j * 4 == y:
            print("Yes")
            exit()
print("No")