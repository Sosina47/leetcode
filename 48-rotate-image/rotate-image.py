class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transposed[col][row] = matrix[row][col]

        for row in transposed:
            row.reverse()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = transposed[row][col]
        