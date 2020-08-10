n = int(input())
s = list(map(int, input()))
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            preindex = 0
            flag1 = 0
            flag2 = 0
            flag3 = 0 
            while preindex < n:
                if s[preindex] == i:
                    preindex += 1
                    flag1 = 1
                    break
                preindex += 1

            while preindex < n:
                if s[preindex] == j:
                    preindex += 1
                    flag2 = 1
                    break
                preindex += 1

            while preindex < n:
                if s[preindex] == k:
                    flag3 = 1
                    break
                preindex += 1
            if flag1 and flag2 and flag3:
                ans += 1
print(ans)
             

