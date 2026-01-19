from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]
        
        def check(i, j, k):
            target = row_sum[i][j + k] - row_sum[i][j]
            for x in range(i, i + k):
                if row_sum[x][j + k] - row_sum[x][j] != target:
                    return False
            for y in range(j, j + k):
                if col_sum[i + k][y] - col_sum[i][y] != target:
                    return False
            if sum(grid[i + d][j + d] for d in range(k)) != target:
                return False
            if sum(grid[i + d][j + k - 1 - d] for d in range(k)) != target:
                return False
            return True
        
        res = 1
        for k in range(2, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if check(i, j, k):
                        res = k
        return res
