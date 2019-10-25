strN = input()
n = int(strN)
for i in range(n,n + 111):
    if i % 111 == 0:
        print(i)
        exit()
