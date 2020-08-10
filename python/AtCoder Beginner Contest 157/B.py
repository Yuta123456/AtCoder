bingo = []
for i in range(3):
    bingo.append(list(map(int, input().split())))
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if bingo[j][k] == b:
                bingo[j][k] = None
for i in range(3):
    row = True
    column = True
    for j in range(3):
        if bingo[i][j] != None:
            column = False
        if bingo[j][i] != None:
            row = False
    if column or row:
        print("Yes")
        exit()
naname = False
if bingo[0][0] == bingo[1][1] == bingo[2][2] == None or bingo[0][2] == bingo[1][1] == bingo[2][0] == None:
    naname = True
if row or column or naname:
    print("Yes")
else:
    print("No")
