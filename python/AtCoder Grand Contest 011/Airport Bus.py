import bisect
import math
n, c, k = list(map(int, input().split()))
t = [0] * n
for i in range(n):
    t[i] = int(input())
t.sort()
bus_count = 0
pre_index = 0
index = 0
while index < n:
    #indexを乗せるバスが発車する時間
    leave = t[index] + k
    count = 0
    bus_count += 1
    while index < n and count < c and leave >= t[index]:
        count += 1
        index += 1
print(bus_count)