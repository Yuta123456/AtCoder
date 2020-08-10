import re
t = int(input())
for case in range(1,t+1):
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    strings.sort(key=lambda x: len(x),reverse=True)
    sample = strings[0].replace("*",'')
    ans = ""
    for word in strings[1:]:
        pattern = word
        pattern = pattern.replace('*', '(\w)*')
        pattern = pattern
        m = re.match(pattern,sample)
        if m:
            if len(m.group()) >= len(ans):
                ans = m.group()
            continue
        else:
            print("Case #{}: *".format(case))
            break
    if m:
        print("Case #{}: {}".format(case,ans))

"""
4
H*O
HELLO*
*HELLO
HE*
2
CO*DE
J*AM
2
CODE*
*JAM
2
A*C*E
*B*D*
2
**Q**
*A*
"""