s = input()
t = input()
for i in range(len(s)):
    tmp = s[i]
    s += tmp
    if s[i+1:] == t:
        print("Yes")
        exit()
print("No")
