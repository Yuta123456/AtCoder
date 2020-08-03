a, b = input().split()
if 999 - int(a) > int(b) - 100:
    a = list(a)
    index = 0
    while index < 3 and a[index] == "9":
        index += 1
    if index != 3:
        a[index] = "9"
else:

    b = list(b)
    if b[0] != "1":
        b[0] = "1"
    elif b[1] != "0":
        b[1] = "0"
    else:
        b[2] = 0
print(int("".join(map(str, a))) - int("".join(map(str, b))))