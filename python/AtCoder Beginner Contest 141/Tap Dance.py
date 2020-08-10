s = input()
odd = []
even = []
for i in range(len(s)):
    if i % 2 == 0:
        odd.append(s[i])
    else:
        even.append(s[i])
if 'L' in odd:
    print("No")
    exit()
elif 'R' in even:
    print("No")
    exit()
print("Yes")
