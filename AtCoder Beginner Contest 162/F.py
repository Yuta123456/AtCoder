n = int(input())
a = list(map(int, input().split()))
dp = [None for i in range(n)]
def calc