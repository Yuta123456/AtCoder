s = input()
win = 0
lose = 0
for i in range(len(s)):
    if i % 2 == 0:
        my = "g"
    else:
        my = "p"
    if my == "g" and s[i] == "p":
        lose += 1
    elif my == 'p' and s[i] == 'g':
        win += 1
print(win -lose)