a,b,k,l = map(int, input().split())
if a*l <= b:
    print(a*k)
else:
    par_set = k //l
    rem = k % l
    if rem * a >= b:
        print(((k//l) + 1) * b)
    else:
        print(par_set*b + rem * a) 