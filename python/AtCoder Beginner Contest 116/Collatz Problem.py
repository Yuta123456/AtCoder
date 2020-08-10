s = int(input())
data = []
data.append(0)
data.append(s)
i = 0
while True:
    i += 1
    if data[i] % 2 == 0:
        data.append(data[i] // 2)
    else:
        data.append((3 * data[i]) + 1)
    if data[i + 1] in data[:i]:
        print(i + 1)
        exit()
