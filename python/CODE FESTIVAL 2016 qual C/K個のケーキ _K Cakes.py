k, t = list(map(int, input().split()))
a = list(map(int, input().split()))
a_max = max(a)
print(max(a_max - 1 - (k - a_max), 0))