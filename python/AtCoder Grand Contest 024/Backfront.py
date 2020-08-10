n = int(input())
p = []
for i in range(n):
    p.append(int(input()))
chain_length = [-1 for i in range(n+1)]
for i in p:
    if chain_length[i-1] < 0:
        chain_length[i] = 1
    else:
        chain_length[i] = chain_length[i-1] + 1
print(n - max(chain_length))
