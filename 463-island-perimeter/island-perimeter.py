class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = [[False] * m for _ in range(n)]

        def outbound(i, j):
            return not(0 <= i < n and 0 <= j < m)

        stack = []
        first = False

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited[i][j] = True

                    stack.append((i, j))
                    first = True
                    break

            if first:
                break
        
        perimeter = 0

        while stack:
            i, j = stack.pop()

            for dr, dc in directions:
                nr = i + dr 
                nc = dc + j

                if outbound(nr, nc) or grid[nr][nc] == 0:
                    perimeter += 1

                elif not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))

        return perimeter

            

                    