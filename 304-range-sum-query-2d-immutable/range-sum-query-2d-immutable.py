class NumMatrix:

    def __init__(self, matrix: List[List[int]]):      
        self.matrix = matrix  

        for i in range(len(self.matrix)):
            self.matrix[i].append(0)
        self.matrix.append([0] * len(self.matrix[0])) 

        for r in range(len(self.matrix) - 1):
            for c in range(len(self.matrix[0]) - 1):

                if r == 0 and c == 0:
                    continue
                self.matrix[r][c] += self.matrix[r][c - 1] + self.matrix[r - 1][c] - self.matrix[r - 1][c - 1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return (self.matrix[row2][col2] - self.matrix[row2][col1 - 1] 
                - self.matrix[row1 - 1][col2] + self.matrix[row1 - 1][col1 - 1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)