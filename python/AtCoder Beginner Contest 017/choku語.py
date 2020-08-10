x = input()
def check(s):
    if s == x:
        print("YES")
        exit()
    if len(s) < len(x):
        flag = True
        for i in range(len(s)):
            if s[i] != x[i]:
                flag = False
                break
        if flag:
            check(s+'ch')
            check(s+'o')
            check(s+'k')
            check(s+'u')
check('')
print("NO")