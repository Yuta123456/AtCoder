import itertools
n = int(input())
lis = ["a","b","c"]
for i in itertools.product(lis, repeat = n):
    for j in range(n):
        print("{}".format(i[j]), end="")
    print()
