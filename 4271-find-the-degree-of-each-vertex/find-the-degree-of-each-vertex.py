class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        output = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                if matrix[i][j] == 1: 
                    output[i] += 1
                    output[j] += 1

        return output