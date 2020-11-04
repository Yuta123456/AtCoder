n = int(input())
point = []
for i in range(n):
    point.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            bec_x = point[i][0] - point[j][0]
            bec_y = point[i][1] - point[j][1]
            bec_q = point[i][0] - point[k][0]
            bec_p = point[i][1] - point[k][1]
            if bec_x == 0 and bec_q == 0:
                print("Yes")
                exit()
            elif bec_x == 0:
                continue
            else:
                cc = bec_q / bec_x
            if bec_y * cc == bec_p:
                #print(point[i], point[j], point[k])
                #print("({}, {}) ({},{})".format(bec_x, bec_y, bec_q, bec_p))
                print("Yes")
                exit()
print("No")