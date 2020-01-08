n = int(input())
candidate = {}
for i in range(n):
    s = input()
    if s in candidate:
        candidate[s] += 1
    else:
        candidate[s] = 1
print(max(candidate, key = lambda x:candidate[x]))
