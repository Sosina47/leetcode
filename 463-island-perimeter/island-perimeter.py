class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = [[False] * m for _ in range(n)]
        perimeter = 0
        
        def outbound(i, j): 
            return i >= n or i < 0 or j >= m or j < 0


        def dfs(i, j):
            nonlocal perimeter

            visited[i][j] = True

            for r, c in directions:
                new_row = i + r
                new_col = j + c

                if outbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    perimeter += 1

                elif not visited[new_row][new_col]:
                    dfs(new_row, new_col)
            
            

        for i in range(n): 
            for j in range(m):

                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter

        return 0