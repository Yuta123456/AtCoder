a, b = list(map(int, input().split()))
def division2(n):
    if(n % 2 == 0):
        return True
    else:
        return False
k = b - a + 1
if division2(k):##戸数が偶数
    if division2(a):
        if division2(k / 2):##個数の半分が偶数
            print(0)
        else:
            print(1)
    else:
        if division2((k - 2)/2):
            print(a ^ b)
        else:
            print(1 ^ a ^ b)
else:
    if division2(a):##最初がguu数
        if division2((k - 1) / 2):
            print(b)
        else:
            print(b ^ 1)
    else:
        if division2((k - 1) / 2):
            print(a)
        else:
            print(a ^ 1)
