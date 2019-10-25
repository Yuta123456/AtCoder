import math
def com(x, y):
    k = math.factorial(x)
    s = math.factorial(y)
    l = math.factorial(x - y)
    return k / (s * l)
