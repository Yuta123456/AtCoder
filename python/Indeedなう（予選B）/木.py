import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
adjacent_list = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
ans = []
candidate = []
heapq.heapify(candidate)
finished = set([1])
def solve(node):
    ans.append(node)
    for i in adjacent_list[node]:
        if not i in finished:
            heapq.heappush(candidate, i)
            finished.add(i)
    if len(candidate) > 0:
        solve(heapq.heappop(candidate))
solve(1)
print(" ".join(map(str, ans)))
