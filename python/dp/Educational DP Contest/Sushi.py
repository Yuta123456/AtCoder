n = int(input())
a = list(map(int, input().split()))
dp = [[[0 for i in range(n)] for j in range(n)] for k in range(n)]

