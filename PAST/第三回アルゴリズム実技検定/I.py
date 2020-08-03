n = int(input())
q = int(input())
row = [i for i in range(n)]
column = [i for i in range(n)]
t_flag = True
for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        row[s[1]-1], row[s[2]-1] = row[s[2]-1], row[s[1]-1]
    elif s[0] == 2:
        column[s[1]-1],  column[s[2]-1] = column[s[2]-1],  column[s[1]-1]
    elif s[0] == 3:
        t_flag = not t_flag
        row, column = column, row
    else:
        if t_flag:
            print(row[s[1]-1] * n +  column[s[2]-1] )
        else:
            print(row[s[1]-1] +  column[s[2]-1] * n)
    """
    print()
    if t_flag:
        for i in range(n):
            for j in range(n):
                print("{}".format(row[i] * n +  column[j]), end = " ")
            print()
    else:
        for i in range(n):
            for j in range(n):
                print("{}".format(row[i] +  column[j] * n), end = " ")
            print()
    """