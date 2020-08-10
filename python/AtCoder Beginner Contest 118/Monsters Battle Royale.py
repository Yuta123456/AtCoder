n = int(input())
a = list(map(int,input().split()))
while True:
    k = min(a)
    i = 0
    while i < len(a):
        if a[i] % k == 0:
            del a[i]
        else:
            a[i] = a[i] % k
            i += 1
    a.append(k)
    if len(a) == 1:
        print(min(a))
        exit()
print(min(a))
