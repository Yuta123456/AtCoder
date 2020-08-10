w, h, n = list(map(int, input().split()))
data1 = [0]
data2 = [w]
data3 = [0]
data4 = [h]
for i in range(n):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        data1.append(x)
    elif a == 2:
        data2.append(x)
    elif a == 3:
        data3.append(y)
    else:
        data4.append(y)
data1.sort()
data2.sort()
data3.sort()
data4.sort()
x = (data2[0] - data1[-1])
y = (data4[0] - data3[-1])
if x < 0 or y < 0:
    print(0)
    exit()
print(x*y)
