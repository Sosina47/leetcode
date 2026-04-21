class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        stack = []

        for i in range(n): 
            for j in range(m):

                if grid[i][j] == '1':
                    grid[i][j] == '0'

                    stack.append((i, j))
                    count += 1

                    while stack: 
                        r, c = stack.pop()

                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc

                            if inbound(nr, nc) and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                stack.append((nr, nc))

        return count

