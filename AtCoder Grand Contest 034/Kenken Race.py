n, a, b, c, d = input().split()
s = input()
flag = False
for i in range(s):
    if flag:
        print("No")
        exit()
    if s[i] == '#':
        flag = True
    else:
        flag = False
if c < d:
