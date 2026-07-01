from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]):
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        pq = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        while pq:
            saf, x, y = heapq.heappop(pq)
            saf = -saf
            if x == n - 1 and y == n - 1:
                return saf
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(pq, (-min(saf, dist[nx][ny]), nx, ny))
        return 0