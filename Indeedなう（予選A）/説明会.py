import bisect
import sys
input = sys.stdin.readline
n = int(input())
student_scores = []
score = [0 for i in range(10**7+1)]
for _ in range(n):
    s = int(input())
    if s != 0:
        score[s+1] += 1
    else:
        n -= 1
for i in range(1,len(score)):
    score[i] += score[i-1]
q = int(input())
for i in range(q):
    amount = n - int(input())
    print(bisect.bisect_left(score, amount))