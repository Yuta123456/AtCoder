h,w,k = map(int, input().split())
mod = 10**9+7
row_amida = []
def make_amida(pre, li):
	if len(li) == w-1:
		row_amida.append(li)
	else:
		if pre == 0:
			make_amida(1, li + [1])
		make_amida(0, li + [0])
make_amida(0,[])
dp = [[0 for i in range(w+1)] for j in range(h+1)]
dp[0][1] = 1 #dp[i][j] := i行目まで決めたときのj列目にたどり着くあみだの本数
for i in range(1,h+1):
	for j in range(1,w+1):
		left_to_cur = 0
		up_to_cur = 0
		right_to_cur = 0
		for p in range(len(row_amida)):
			upflag = True
			if j != 1 and row_amida[p][j-2] == 1:
				left_to_cur += 1
				upflag = False
			if j != w and row_amida[p][j-1] == 1:
				right_to_cur += 1
				upflag = False
			if upflag:
				up_to_cur += 1
		if j != 1:
			left_to_cur = (left_to_cur * dp[i-1][j-1]) % mod
		if j != w:
			right_to_cur = (right_to_cur * dp[i-1][j+1]) % mod
		up_to_cur = (up_to_cur * dp[i-1][j]) % mod
		dp[i][j] = right_to_cur + left_to_cur + up_to_cur
		dp[i][j] %= mod
print(dp[-1][k])







  
