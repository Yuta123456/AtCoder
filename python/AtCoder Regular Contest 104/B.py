n, s = input().split()
n = int(n)
acc = [[0 for i in range(4)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(4):
        acc[i][j] += acc[i-1][j]
    if s[i-1] == 'A':
        acc[i][0] += 1
    elif s[i-1] == 'T':
        acc[i][1] += 1
    elif s[i-1] == 'C':
        acc[i][2] += 1
    else:
        acc[i][3] += 1
#print(acc)
ans = 0
for i in range(n):
   for j in range(i+1, n):
       a = acc[j+1][0] - acc[i][0]
       t = acc[j+1][1] - acc[i][1]
       c = acc[j+1][2] - acc[i][2]
       g = acc[j+1][3] - acc[i][3]
       #print("i:{} j:{} a:{} g:{} c:{} t:{}".format(i,j,a,g,c,t))
       if a == t and c == g:
           ans += 1
print(ans)
