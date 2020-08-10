data = list(map(int, input().split()))
if sum(data) % 2 == max(data) % 2:
    print(( max(data) * 3 - sum(data) )  // 2)
else:
    print(((max(data) + 1) * 3 - sum(data)) // 2)
