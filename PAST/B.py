n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(1,n):
    if a[i] - a[i-1] < 0:
        s = "down"
    elif a[i] - a[i-1] > 0:
        s = "up"
    else:
        print("stay")
        continue
    print("{} {}".format(s, abs(a[i] - a[i-1])))