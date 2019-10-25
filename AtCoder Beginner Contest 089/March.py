n = int(input())
data = [0 for i in range(5)]
for i in range(n):
    k = input()
    if k[0] == 'M':
        data[0] += 1
    elif k[0] == 'A':
        data[1] += 1
    elif k[0] == 'R':
        data[2] += 1
    elif k[0] == 'C':
        data[3] += 1
    elif k[0] == 'H':
        data[4] += 1
total = 0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            total += data[i] * data[j] * data[k]
print(total)
