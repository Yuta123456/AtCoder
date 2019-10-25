n = int(input())
i = 0
j = 0
k = 0
while k < 100:
    while k < 100:
        k = i * 4 + j * 7
        if k == n:
            print("Yes")
            exit()
        j += 1
    j = 0
    k = i * 4 + j * 7
    i += 1
print("No")
