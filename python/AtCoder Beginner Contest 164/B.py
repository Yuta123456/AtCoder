a,b,c,d = map(int, input().split())
takahashi = 1
while True:
    if takahashi:
        c -= b
    else:
        a -= d
    takahashi = 1- takahashi 
    if c <= 0:
        print("Yes")
        exit()
    if a <= 0:
        print("No")
        exit()