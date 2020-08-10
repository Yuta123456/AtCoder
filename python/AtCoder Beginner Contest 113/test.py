n,m = map(int, input().split())
py = []
for i in range(m):
  a,b = map(int, input().split())
  py.append([a,b,i])
py.sort()
p = py[0][0]
y = 1
for i in range(m):
  if py[i][0] == p:
    py[i][1] = y
    y += 1
  else:
    py[i][1] = 1
    y = 2
    p = py[i][0]
py = sorted(py, key=lambda x:x[2])
for p,y,i in py:
  print("{:0=6}{:0=6}".format(p,y))
