class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = []
        for i in range(len(grid)):
            row_max.append(max(grid[i]))

        col_max = []
        for i in range(len(grid[0])):
            temp = float("-inf")
            for j in range(len(grid)):
                temp = max(temp, grid[j][i])
            col_max.append(temp)

        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(row_max[i], col_max[j]) - grid[i][j]

        return total