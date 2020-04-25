k = input()
hand = [set() for i in range(4)]
s = []
for i in range(len(k)):
    if k[i] in set(['S','H','D','C']):
        if i + 2 < len(k) and k[i+1:i+3] == '10':
            s.append(k[i:i+3])
        else:
            s.append(k[i:i+2])

ans = -1
fin = -1
for k,i in enumerate(s):
    flag = False
    mark = i[0]
    num = i[1:]
    if mark == 'S':
        hand[0].add(num)
        if '10' in hand[0] and 'J' in hand[0] and 'Q' in hand[0] and 'K' in hand[0] and 'A' in hand[0]:
            ans = mark
            fin = k
            break
    elif mark == 'H':
        hand[1].add(num)
        if '10' in hand[1] and 'J' in hand[1] and 'Q' in hand[1] and 'K' in hand[1] and 'A' in hand[1]:
            ans = mark
            fin = k
            break
    elif mark == 'D':
        hand[2].add(num)
        if '10' in hand[2] and 'J' in hand[2] and 'Q' in hand[2] and 'K' in hand[2] and 'A' in hand[2]:
            ans = mark
            fin = k
            break
    else:
        hand[3].add(num)
        if '10' in hand[3] and 'J' in hand[3] and 'Q' in hand[3] and 'K' in hand[3] and 'A' in hand[3]:
            ans = mark
            fin = k
            break
flag = True
for k,i in enumerate(s):
    mark = i[0]
    num = i[1:]
    if k == fin:
        break
    if ans == mark:
        if num == '10' or num == 'J' or num == 'Q' or num == 'K' or num == 'A':
            continue
        else:
            flag = False
            print(i,end="")
    else:
        flag = False
        print(i,end="")
if flag:
    print(0)
    exit()
else:
    print()