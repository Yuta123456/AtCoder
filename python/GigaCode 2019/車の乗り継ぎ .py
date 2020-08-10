from collections import deque
n, l = map(int, input().split())
vs, ds = map(int, input().split())
data = deque()
use_car = []
for i in range(n):
    x,v,d = map(int, input().split())
    data.append([x,v,d])
data = sorted(data, key = lambda x:x[0])
dp = [0 for i in l]
for i in range(len(data)):
    

