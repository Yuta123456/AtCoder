
n, m = list(map(int, input().split()))
data = [[]]
i = 2
count = 0
while m > 1:
    if m % i == 0:
        count = 0
        while m % i == 0:
            m = m/i
            count += 1
            if m % i != 0:
                break
    data.append(list(i, count))
print(data)
