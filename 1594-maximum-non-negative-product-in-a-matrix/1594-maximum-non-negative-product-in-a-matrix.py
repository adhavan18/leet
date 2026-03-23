class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ROWS, COLS = len(grid), len(grid[0])

        dp_max = [[0] * COLS for _ in range(ROWS)]
        dp_min = [[0] * COLS for _ in range(ROWS)]

        dp_max[0][0] = dp_min[0][0] = grid[0][0]

        for i in range(1, ROWS):
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]

        for j in range(1, COLS):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                val = grid[i][j]

                candidates = [
                    dp_max[i-1][j] * val,
                    dp_min[i-1][j] * val,
                    dp_max[i][j-1] * val,
                    dp_min[i][j-1] * val
                ]

                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)

        result = dp_max[ROWS-1][COLS-1]

        if result < 0:
            return -1
        return result % MOD