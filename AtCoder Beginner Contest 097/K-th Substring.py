s = list(input())
k = int(input())
candidate = []
for i in range(len(s)):
    for j in range(k+1):
        candidate.append(s[i:i+j])
for i in range(len(candidate)):
    candidate[i] = "".join(candidate[i])
candidate = list(set(candidate))
def sort_key(x):
    while len(x) < 5:
        x += "_"
    return x
candidate.sort(key = sort_key)
print(candidate[k])