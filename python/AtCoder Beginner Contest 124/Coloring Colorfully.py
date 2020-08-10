s = input()
n = len(s)
count = 0
data = []
for i in range(n):
    data.append(int(s[i]))
for  i in range(n -1):
    if data[i] == data[i + 1]:
        data[i + 1] = (data[i + 1] + 1) % 2
        count += 1
print(count)
