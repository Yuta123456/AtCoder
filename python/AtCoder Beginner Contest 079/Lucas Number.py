n = int(input())
L = [0 for i in range(100)]
L[0] = 2
L[1] = 1
def Lucas(n):
    if L[n] != 0:
        return L[n]
    else:
        L[n - 1] = Lucas(n - 1)
        L[n - 2] = Lucas(n - 2)
        return L[n - 1] + L[n - 2]
print(Lucas(n))
