import numpy as np
class info:
    def __init__(self):
        self.kind = set()
        self.bp = 0
        self.total = 0
    def calc(self):
        self.kind = (len(self.kind)) * 2 + self.bp


n, k = list(map(int, input().split()))
t = []
d = []
for i in range(n):
    s = list(map(int, input().split()))
    t.append(s[0])
    d.append(s[1])

dp = np.empty(n + 1, k, dtype = info)
for i in range(k):
    for j in range(1, n + 1):
