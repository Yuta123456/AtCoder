s = input()
word = [0 for i in range(26)]
for i in range(len(s)):
    word[ord(s[i]) - ord('a')] += 1
one = 0
even = 0
for i in range(26):
    if word[i] == 1:
        one += 1
    elif word[i] % 2 == 1:
        even += (word[i] - 1)
        one += 1
    else:
        even += word[i]
if one == 0:
    print(even)
    exit()
ans = ((even / 2) // one)
print(int(ans*2 + 1))