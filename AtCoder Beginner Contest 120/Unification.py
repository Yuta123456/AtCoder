s = input()
data = []
for i in s:
    data.append(int(i))
one = 0
zero = 0
for i in range(len(data)):
    if data[i] == 0:
        zero += 1
    else:
        one += 1

print(min(zero, one) * 2)
