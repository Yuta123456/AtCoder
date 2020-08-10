x = int(input())
money = 100
for i in range(3800):
    money = int(money)
    if  money >= x:
        print(i)
        exit()
    money *= 1.01