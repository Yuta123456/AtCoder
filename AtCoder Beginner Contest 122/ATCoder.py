s = input()
max = ''
for i in range(len(s)):
    for j in range(len(s)):
        flag = True
        judge = s[i:j+1]
        for k in judge:
            if k != "A" and k != "C" and k != "G" and k != "T":
                flag = False
                break
        if flag and len(judge) > len(max):
            max = judge
print(len(max))
