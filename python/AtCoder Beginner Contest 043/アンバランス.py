s = input()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print("{} {}".format(i+1, i+2))
        exit()
    if i < len(s) - 2:
        if s[i] == s[i+2]:
            print("{} {}".format(i+1, i+3))
            exit()
print("{} {}".format(-1,-1))