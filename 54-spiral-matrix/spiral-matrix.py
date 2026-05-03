class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        vis = [[False] * n for _ in range(m)]

        #change in row index for each direction
        dr = [0, 1, 0, -1]

        #change in column index for each direction
        dc = [1, 0, -1, 0]

        r, c = 0, 0
        idx = 0
        for _ in range(m*n):
            res.append(matrix[r][c])
            vis[r][c] = True

            newR, newC = r + dr[idx], c + dc[idx]
            if 0 <= newR < m and 0 <= newC < n and not vis[newR][newC]:
                r, c = newR, newC
            else:
                idx = (idx + 1) % 4
                r += dr[idx]
                c += dc[idx]
        return res