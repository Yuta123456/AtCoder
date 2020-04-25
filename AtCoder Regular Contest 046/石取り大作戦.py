n = int(input())
a,b = map(int, input().split())
#残りi個の時、高橋君が勝つ→True 負ける->False
dp = [False for i in range(n+1)]
