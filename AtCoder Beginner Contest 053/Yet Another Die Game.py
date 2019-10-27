x = int(input())
if x % 11 == 0:
    print((x // 11) * 2)
elif 6 < x and x < 11:
    print(2)
elif x <= 6:
    print(1)
else:
    if x % 11 > 6:
        print((x // 11) * 2 + 2)
    else:
        print((x // 11) * 2 + 1)