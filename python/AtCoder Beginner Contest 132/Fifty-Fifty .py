s = input()
count = 0
for i in range(4):
    for j in range(4):
        if s[i] == s[j]:
            count += 1
if count == 8:
    print("Yes")
else:
    print("No")
