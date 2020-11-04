t = int(input())
ATCODER = "atcoder"
for _ in range(t):
    s = list(input())
    in_not_a = False
    index = -1
    t_less = -1
    for i in range(len(s)):
        if s[i] != 'a':
            in_not_a = True
            index = i
            if s[i] > 't':
                t_less = i
            break
    if s[0] != 'a':
        print(0)
    elif in_not_a:
        if "".join(s) > ATCODER:
            print(0)
        else:
            if t_less != -1:
                print(t_less-1)
            else:
                print(index)
    else:
        print(-1)

    
    
    