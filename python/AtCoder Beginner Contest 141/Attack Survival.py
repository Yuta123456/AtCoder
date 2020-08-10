n, k , q = list(map(int, input().split()))
answer = [0 for i in range(n)]
for i in range(q):
    answer[int(input()) - 1] += 1
for i in range(n):
    if k - (q - answer[i]) > 0:
        print("Yes")
    else:
        print("No")
