String  = input()
index = 0
flag = False
while index < len(String) - 1:
    flag = True
    if String[index:index + 7] == "dreamer":
        index += 7
        if String[index:index + 4] == "aser":
            index += 4
        elif String[index:index + 3] == "ase":
            index += 3
    elif String[index:index + 5] == "dream":
            index += 5
    elif String[index:index + 6] == "eraser":
            index += 6
            if String[index:index + 4] == "aser":
                index += 4
            elif String[index:index + 3] == "ase":
                index += 3
    elif String[index:index + 5] == "erase":
                index += 5
    else:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
