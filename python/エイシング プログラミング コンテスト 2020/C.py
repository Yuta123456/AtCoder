n = int(input())
ans = [0 for i in range(n + 1)]
for x in range(1,int(pow(n, 0.5)+1)):
    for y in range(1,int(pow(n, 0.5)+1)):
        for z in range(1,int(pow(n, 0.5)+1)):
            if x**2 + y**2+z**2 +x*y + x*z + y*z <= n:
                ans [x**2 + y**2+z**2 +x*y + x*z + y*z] += 1
for i in range(1,n+1):
    print(ans[i])