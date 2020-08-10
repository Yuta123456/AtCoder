n, k = map(int, input().split())
child = (n - k) * (k - 1) * 6
child += n * 3
child -= 2
parent = n**3
print(child/parent)