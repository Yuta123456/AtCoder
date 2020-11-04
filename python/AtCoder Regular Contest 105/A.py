c = list(map(int, input().split()))
sum_all = sum(c)
for i in range(2):
    for j in range(2):
        for k in range(2):
            for p in range(2):
                count = 0
                ooo = sum_all
                if i == 1:
                    count += c[0]
                    ooo -= c[0]
                if j == 1:
                    count += c[1]
                    ooo -= c[1]
                if k == 1:
                    count += c[2]
                    ooo -= c[2]
                if p == 1:
                    count += c[3]
                    ooo -= c[3]
                if count == ooo:
                    print("Yes")
                    exit()             
print("No")                