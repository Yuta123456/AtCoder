s = input()
min = 753
for i in range(len(s) - 2):
    k = int(s[i:i+3])
    if min > abs(753 - k):
        min = abs(753 - k)
print(min)
