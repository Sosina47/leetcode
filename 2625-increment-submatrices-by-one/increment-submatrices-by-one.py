class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * (n + 1) for _ in range(n + 1)]

        for row1, col1, row2, col2 in queries:
            matrix[row1][col1] += 1
            matrix[row2 + 1][col1] -= 1
            matrix[row1][col2 + 1] -= 1
            matrix[row2 + 1][col2 + 1] += 1

        for i in range(n + 1):
            matrix[i][-1] = 0
        matrix[-1] = [0] * (n + 1)

        for r in range(n):
            for c in range(n):
                matrix[r][c] += matrix[r][c - 1] + matrix[r - 1][c] - matrix[r - 1][c - 1]

        for i in range(n):
            matrix[i].pop()
        matrix.pop()

        return matrix