n,s = map(int, input().split())
a = list(map(int, input().split()))
mod = 998244353
#最終的に、f(1,1) - f(n,n)が全て求まっている状態で、二重ループを回す
