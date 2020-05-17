n = int(input())
data = []
for i in range(n):
    s = input()
    k = len(s) - s.count(')')*2
    data.append([k,s])
data.sort(reverse=True,key=lambda x: x[0])
ans = 0
for i in range(len(data)):
    s = data[i][1]
    for j in range(len(s)):
        if s[j] == '(':
            ans += 1
        else:
            ans -= 1
        if ans < 0:
            print("No")
            exit()
if ans == 0:
    print("Yes")
else:
    print("No")

