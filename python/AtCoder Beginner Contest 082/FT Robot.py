s = input()
x, y = map(int, input().split())
totalx = 0
totaly = 0
shift_x = []
shift_y = []
index = 0
while s[index] != "T" and index +1< len(s):
    totalx += 1
    index += 1
flag = 1
count = 0
for i in range(index, len(s)):
    if s[i] == "T":
        if flag == 1:
            shift_x.append(count)
        else:
            shift_y.append(count)
        flag *= -1
        count = 0
    else:
        count += 1
if flag == 1:
    shift_x.append(count)
else:
    shift_y.append(count)
shift_x.sort()
shift_x.reverse()
shift_y.sort()
shift_y.reverse()
for i in range(len(shift_x)):
    if totalx < x:
        totalx += shift_x[i]
    else:
        totalx -= shift_x[i]
for i in range(len(shift_y)):
    if totaly < y:
        totaly += shift_y[i]
    else:
        totaly -= shift_y[i]
if totalx == x and totaly == y:
    print("Yes")
else:
    print("No")