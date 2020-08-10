
n = int(input())
T = 45
F = 19
a = [[0 for i in range(F)] for j in range(T)]
p = pow(10,9)
two_size = 18
five_size = 18
count = 0
for i in range(n):
    s = input()
    if '.' in s:
        index = s.index('.')
        s += '0' * (  9 - (len(s) - 1 - index))
        s = s.replace('.','')
    else :
        s += '0' * 9
    k = int(s)
    two = 0
    five = 0
    while k % 2 == 0:
        two += 1
        k //= 2
    while k % 5 == 0:
        five += 1
        k //= 5
    t, f = two_size - two, five_size - five
    for x in range(t, T):
        for y in range(f, F):
            count += a[x][y]
    a[two][five] += 1
print(count)