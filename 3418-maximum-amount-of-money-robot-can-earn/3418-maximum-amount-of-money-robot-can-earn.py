3418

class Solution:
	def maximumAmount(self, coins):
		m, n = len(coins), len(coins[0])
		dp = [[[-float('inf')]*3 for _ in range(n)] for _ in range(m)]
		
		for k in range(3):
			if coins[0][0] >= 0:
				dp[0][0][k] = coins[0][0]
			else:
				dp[0][0][k] = coins[0][0]
				if k > 0:
					dp[0][0][k] = 0
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0:
					continue
				for k in range(3):
					best = -float('inf')
					if i > 0:
						best = max(best, dp[i-1][j][k])
					if j > 0:
						best = max(best, dp[i][j-1][k])
					dp[i][j][k] = best + coins[i][j]
					
					if coins[i][j] < 0 and k > 0:
						best_prev = -float('inf')
						if i > 0:
							best_prev = max(best_prev, dp[i-1][j][k-1])
						if j > 0:
							best_prev = max(best_prev, dp[i][j-1][k-1])
						dp[i][j][k] = max(dp[i][j][k], best_prev)
		return max(dp[m-1][n-1])
		
					
		 