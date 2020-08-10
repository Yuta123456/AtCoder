def solve(list):
    res = 10000
    print(list)
    if len(list) <= 2:
        return list[0] + list[1]
    else:
        for i in range(1, len(list) - 1):
            a = list
            a[i - 1] += a[i]
            a[i + 1] += a[i]
            del a[i]
            k = solve(a)
            print("k => {}".format(type(k)))
            print("res => {}".format(type(res)))
            res = min(k, res)
n = int(input())
a = list(map(int, input().split()))
print(solve(a))
