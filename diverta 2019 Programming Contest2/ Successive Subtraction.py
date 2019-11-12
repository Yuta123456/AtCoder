n = int(input())
data = list(map(int, input().split()))
data.sort()
#全て正の時の処理
if data[0] > 0:
    print(sum(data) - data[0] * 2)
    k = data[0]
    for i in range(1,n - 1):
        print("{} {}".format(k, data[i]))
        k -= data[i]
    print("{} {}".format(data[-1], k))
#すべて負の場合の処理
elif data[-1] <= 0:
    print(-sum(data) + (data[-1] * 2))
    k = data[-1]
    for i in range(n - 1):
        print("{} {}".format(k, data[i]))
        k -= data[i]
#それ以外
else: 
    print(sum(list(map(lambda x:abs(x), data))))
    max_data = data[-1]
    min_data = data[0]
    i = 1
    while data[i] <= 0:
        print("{} {}".format(max_data,data[i]))
        max_data -= data[i]
        i += 1
    while i < n - 1:
        print("{} {}".format(min_data, data[i]))
        min_data -= data[i]
        i += 1
    print("{} {}".format(max_data, min_data))


    


