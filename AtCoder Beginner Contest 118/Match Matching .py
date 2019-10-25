n , m = map(int, input().split())
A = list(map(int, input().split()))
table = [0,2,5,5,4,5,6,3,7,6]
dp = [0 for i in range(n + 1)]
for i in range(n):
    
