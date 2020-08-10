n, m = map(int , input().split())
start = []
goal = []
for i in range(m):
    a, b = list(map(int, input().split()))
    if a == 1:
        start.append(b)
    elif b == n:
        goal.append(a)
if len(set(start) & set(goal)) >= 1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")