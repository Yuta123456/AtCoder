n, a, b, c, d = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1
s = input()
flag = False
for i in range(a,c):
    if s[i] == s[i+1] == '#':
        print("No")
        exit()
for i in range(b,d):
    if s[i] == s[i+1] == '#':
        print("No")
        exit()
if c < d:
    print("Yes")
else:
    for i in range(b, d+1):
        if s[i-1] == '.' and s[i] == '.' and s[i+1] == '.':
            print("Yes")
            exit()
    print("No")

