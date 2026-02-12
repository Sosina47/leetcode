class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        transposed = [[0 for _ in range(r)] for _ in range(c)]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transposed[col][row] =  matrix[row][col]
            

        return transposed 