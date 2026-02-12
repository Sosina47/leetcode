class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for row in range(len(matrix)):
            if 0 in matrix[row]:
                rows.add(row)
            
            for col in range(len(matrix[0])):
                if col not in cols and matrix[row][col] == 0:
                    cols.add(col)

        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])): 
                if row in rows:
                    matrix[row][col] = 0
                
                elif col in cols:
                    matrix[row][col] = 0

        