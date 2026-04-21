class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * m for _ in range(n)]

        count = 0

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            for dr, dc in directions:
                nr = i + dr
                nc = j + dc

                if inbound(nr, nc) and grid[nr][nc] == '1' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    dfs(nr, nc)

            

        for i in range(n): 
            for j in range(m):

                if grid[i][j] == '1' and not visited[i][j] and inbound(i, j):
                    visited[i][j] = True
                    count += 1

                    dfs(i, j)

        return count