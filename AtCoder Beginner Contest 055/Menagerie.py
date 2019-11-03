import copy
n = int(input())
q = input()
a = ["." for i in range(n)]

def checkAns(data):
    #data[0]の処理
    if data[0] == "S":
        if q[0] == 'o':
            data[-1] = data[1]
        else:
            if data[1] == "S":
                data[-1] = "W"
            else:
                data[-1] = "S"
    else:
        if q[0] != 'o':
            data[-1] = data[1]
        else:
            if data[1] == "S":
                data[-1] = "W"
            else:
                data[-1] = "S"
    
    check = copy.deepcopy(data[-1])
    #その後の処理
    for i in range(1,n-1):
        if data[i] == "S":
            if q[i] == "o":
                data[i+1] = data[i-1]
            else:
                #罰だった場合の処理
                if data[i - 1] == "W":
                    data[i + 1] = "S"
                else:
                    data[i + 1] == "W"
        else:
            if q[i] != "o":
                data[i + 1] = data[i - 1]
            else:
                #罰だった場合の処理
                if data[i - 1] == "W":
                    data[i + 1] = "S"
                else:
                    data[i + 1] == "W"
    if check == data[-1]:
        return data
    else:
        return False
a[0] = "S"
a[1] = "S"
if checkAns(a):
    ans = checkAns(a)
    ans = "".join(ans)
    ans = ans.replace(".", 'W')
    print(ans)
    exit()

a[0] = "S"
a[1] = "W"
if checkAns(a):
    print(a)
    exit()

a[0] = "W"
a[1] = "W"
if checkAns(a):
    print(a)
    exit()

a[0] = "W"
a[1] = "S"
if checkAns(a):
    print(a)
    exit()

print(-1)