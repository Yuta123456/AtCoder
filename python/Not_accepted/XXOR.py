n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
alpha = '0'
b = []
one = 0
zero = 0
for i in range(n):
    b.append(format(a[i], '041b'))
if k == 0:
    print(sum(a))
    exit()
else:
    k = len(format(k,'b'))
i = 0
while int(alpha, 2) < k:
    one = 0
    zero = 0
    for j in range(n):
        if b[j][-1-i] == '1':
            one += 1
        elif b[j][-1-i] == '0':
            zero += 1
    if one > zero:
        alpha  = '0' + alpha
    else:
        alpha  = '1' + alpha
    i += 1
beta = int(alpha[1:-1],2)

sumA = 0
for i in range(n):
    sumA += a[i] ^ beta
print(sumA)
