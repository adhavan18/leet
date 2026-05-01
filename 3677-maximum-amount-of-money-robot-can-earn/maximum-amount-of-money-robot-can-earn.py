class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = max coins at (i,j) using k neutralizations
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Initialize (0,0)
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            else:
                # either take loss or neutralize
                dp[0][0][k] = coins[0][0]
                if k > 0:
                    dp[0][0][k] = 0
        
        # Fill DP
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                for k in range(3):
                    best = -float('inf')
                    
                    # from top
                    if i > 0:
                        best = max(best, dp[i-1][j][k])
                    
                    # from left
                    if j > 0:
                        best = max(best, dp[i][j-1][k])
                    
                    # normal take
                    dp[i][j][k] = best + coins[i][j]
                    
                    # if robber and can neutralize
                    if coins[i][j] < 0 and k > 0:
                        best_prev = -float('inf')
                        
                        if i > 0:
                            best_prev = max(best_prev, dp[i-1][j][k-1])
                        if j > 0:
                            best_prev = max(best_prev, dp[i][j-1][k-1])
                        
                        dp[i][j][k] = max(dp[i][j][k], best_prev)
        
        return max(dp[m-1][n-1])