s = input()
preS = ''
prei = 0
count = 0
i = 0
while i < len(s):
    if s[prei:i] == preS:
        i+= 1
    else:
        count += 1
        prei = i
        preS = s[prei:i]
print(count)
