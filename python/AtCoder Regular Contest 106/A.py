n = int(input())
fin = 0
while pow(5, fin) < n:
    fin += 1
five = 1
for i in range(1,fin):
    five *= 5
    k = n - five
    # print("{} {} {}".format(i, k, five))
    count = 0
    while k != 0 and k % 3 == 0:
        k = k // 3
        count += 1
    if k == 1 and count != 0:
        print("{} {}".format(count, i))
        exit()
print("-1")