n, a, b = map(int, input().split())
print("{} {}".format(min(n, min(a, b)), max(0, (a+b) - n)))
