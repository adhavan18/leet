class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]

        for row1, col1, row2, col2 in queries:
            for r in range(row1, row2 + 1):
                mat[r][col1] += 1
                if col2 + 1 < n:
                    mat[r][col2 + 1] -= 1
        
        for r in range(n):
            for c in range(1,n):
                mat[r][c] += mat[r][c - 1]

        return mat