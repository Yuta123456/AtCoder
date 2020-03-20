import numpy as np
A, B = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0 for i in range(A)] for j in range(B)]
#dp[i][j] := 左の山からi、右の山からjとったときののすぬけくんの点数
for i in range(1,A+1):
    for j in range(1,B+1):
        
