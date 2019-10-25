class ver():
    def __init__(self, num):
        self.neighbor = set()
        self.num = num
        self.P = 0
n, k = list(map(int, input().split()))
a = []
Vertax = []
for i in range(n + 1):
    Vertax.append(ver(i))
for i in range(n - 1):
    a.append(list(map(int, input().split())))
for i in range(n - 1):
    Vertax[a[i][0]].neighbor.add(a[i][1])
    Vertax[a[i][1]].neighbor.add(a[i][0])
count = 1
visited = set()
willVisit = Vertax[1].neighbor
Vertax[1].P = k
while not (willVisit is Null):
    for i in list(willVisit):
        
