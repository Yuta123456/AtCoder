def euqlid(x,y):
    while x % y != 0:
        tmp = x % y
        x = y
        y = tmp
    return y
a, b = map(int, input().split())
if a < b:
    tmp = a
    a = b
    b = tmp
k = euqlid(a, b)
sum = 0
i = 2
while k > 1:
    flag = False
    while k % i == 0:
        k = k // i
        flag = True
    if flag:
        sum += 1
    i += 1
print(sum + 1)
