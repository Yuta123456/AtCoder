import math
n, m = list(map(int, input().split()))
def combi(x, y):
    return math.factorial(x) / (math.factorial(x - y) * math.factorial(y))

print((n - 1) * (m - 1))