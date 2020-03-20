s = input()
flag = True
for i in range(0,len(s),2):
    if s[i:i+2] != 'hi':
        flag = False
if flag:
    print("Yes")
else:
    print("No")