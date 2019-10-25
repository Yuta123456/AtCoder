s = input()
def end():
    print("WA")
    exit()
if s[0] != 'A':
    end()
flag = False
for i in s[2:-1]:
    if i == 'C':
        if flag:
            end()
        flag = True
if not flag:
    end()

flag = False
for i in range(1,len(s)):
    if s[i].isupper():
        if flag:
            end()
        flag = True

print("AC")
