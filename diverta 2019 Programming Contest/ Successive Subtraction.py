n = int(input())
data = list(map(int, input().split()))
data.sort()
sum = 0
if data[0] >= 0:
    sum += lambda i for i in data: abs(i)
    sum -= min(data) * 2
    print(sum)
    for i in range(n - 1):
        print("{} {}".format(max(data), min(data)))
        add = min(data) - max(data)
        del data[data.index(max(data)]
        del data[data.index(min(data))]
        data.append(add)

else if(data[len(data) - 1] <= 0):
    sum += lambda i for i in data: abs(i)
    sum -= max(data) * 2
    print(sum)
    for i in range(n - 1):
        print("{} {}".format(max(data), min(data)))
        add = max(data) - min(data)
        del data[data.index(max(data)]
        del data[data.index(min(data))]
        data.append(add)

else:
    sum += lambda i for i in data: abs(i)
    print(sum)
    for i in range(n - 1):
        print("{} {}".format(max(data), min(data)))
        add = min(data) - max(data)
        del data[data.index(max(data)]
        del data[data.index(min(data))]
        data.append(add)
