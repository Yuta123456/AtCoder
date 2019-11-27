import sys
n,m = map(int,input().split())
#input = sys.stdin.readline
sys.setrecursionlimit(10**9)
list1 = []
s = list(input())
s.reverse()
def maze(mass): #今いるマス、現状の手数
    if mass+m >= n:
        list1.append(n-mass)
        return
    for i in range(m,0,-1):
        if s[mass+i] == "0":
            list1.append(i)
            maze(mass+i)
            return
        elif i == 1:
            print(-1)
            exit()
maze(0)
list1.reverse()
print(" ".join(map(str,list1)))