n,k = map(int, input().split())
word = [0 for i in range(26)]
ans = 0
for i in range(n):
    q = input()
    word[ord(q[0]) - ord('A')] += 1
word.sort(reverse=True)
for i in range(n//k):
    for j in range(k):
        word[j] -= 1
        if word[j] < 0:
            print(ans)
            exit()
    ans += 1
    word.sort(reverse=True)
print(ans)