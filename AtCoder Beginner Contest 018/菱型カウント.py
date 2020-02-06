import sys 
input = sys.stdin.readline
r,c,k = map(int, input().split())
grid = []
def check(s,t):
    if (0 <= s <= c - 1) and (0 <= t <= r - 1):
        return True
    else:
        return False
