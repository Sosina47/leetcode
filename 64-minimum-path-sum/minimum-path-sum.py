class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # f = float('inf')
        # for i in range(len(grid)):
        #     grid[i].append(f)
        # grid.append([f] * (len(grid[0]) + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue

                if i == 0:
                    grid[i][j] += grid[i][j - 1]

                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] = min(grid[i][j] + grid[i - 1][j], grid[i][j] + grid[i][j - 1])

        return grid[-1][-1]