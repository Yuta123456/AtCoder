h, w, s ,v = map(int, input().split())
data = [[] for i in range(h)]
for i in range(h):
    data[i] = list(map(int, input().split()))
max_area = 0
for i in range(h):
    for j in range(w):
        for k in range(i,h):
            for l in range(j, w):
                total = 0
                print("i {}  j{} k {} l {}".format(i,j,k,l))
                for m in range(i,k+1):
                    for q in range(j,l+1):
                        total += data[m][q]
                mmm = total + s * (k - i) * (l - j)
                if mmm <= v and (1+k-i) * (1+l-j) > max_area:
                    max_area = (1+k-i) * (1+l-j)
print(max_area)
