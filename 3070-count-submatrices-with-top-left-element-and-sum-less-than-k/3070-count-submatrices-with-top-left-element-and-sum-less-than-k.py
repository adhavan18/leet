class Solution:
    def countSubmatrices(self, matrix, k):
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = [[0] * COLS for _ in range(ROWS)]
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 and j == 0:
                    dp[i][j] = matrix[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + matrix[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + matrix[i][j]
                else:
                    dp[i][j] = (
                    dp[i][j - 1]
                    + dp[i - 1][j]
                    - dp[i - 1][j - 1]
                    + matrix[i][j]
                )
            
                if dp[i][j] <= k:
                    ans += 1
    
        return ans  