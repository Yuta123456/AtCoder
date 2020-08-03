n = int(input())
x = input()
mod_num1 = [0 for i in range(n+1)]
mod_num2 = [0 for i in range(n+1)]
mod_num3 = [0 for i in range(n+1)]
num2 = x.count('1')
if num2 == 0:
    for i in range(n):
        print(1)
    exit()
elif num2 == 1:
    index = x.index('1')
    for i in range(n):
        if x[i] == '1':
            print(0)
        else:
            if index == n-1 or i == n-1:
                print(2)
            else:
                print(1)
    exit()
num1 = num2 - 1
num3 = num2 + 1
for i in range(n):
    if x[i] == '1':
        mod_num1[i] = pow(2, n-i-1 ,num1)
        mod_num2[i] = pow(2, n-i-1, num2)
        mod_num3[i] = pow(2, n-i-1, num3)
def popcount(num):
    res = 0
    while num != 0:
        res += 1
        num = num % "{:b}".format(num).count('1')
    return res
s_1 = sum(mod_num1)
s_2 = sum(mod_num2)
s_3 = sum(mod_num3)
for i in range(n):
    if x[i] == '1':
        print(popcount((s_1 - pow(2, n-i-1, num1)) % num1) + 1)
    else:
        print(popcount((s_3 + pow(2, n-i-1, num3)) % num3) + 1)


