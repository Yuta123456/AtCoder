n = int(input())
num = 26
alphabet =  [chr(ord('a') + i) for i in range(26)]
ans = []
while n > 0:
    n -= 1
    ans += alphabet[n % num]
    n = n // num
    
ans.reverse()
print("".join(ans))