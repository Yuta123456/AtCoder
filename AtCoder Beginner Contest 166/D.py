x = int(input())
for i in range(-1000,1000+1):
    for j in range(-1000,1001):
        if pow(i,5) - pow(j,5) == x:
            print("{} {}".format(i,j))
            exit()