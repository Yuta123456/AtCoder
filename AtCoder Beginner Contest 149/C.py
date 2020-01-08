x = int(input())
def check(n):
    for i in range(2,int(x**0.5) + 1):
        if n % i == 0:
            return False
    return True
while True:
    if check(x):
        print(x)
        exit()
    x += 1