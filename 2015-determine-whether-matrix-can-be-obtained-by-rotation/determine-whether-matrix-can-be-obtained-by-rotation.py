class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        rotated = [[0] * len(mat[0]) for _  in range(len(mat))]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                rotated[col][row] = mat[row][col]

        for row in rotated:
            row.reverse()

        if target == rotated: 
            return True

        for row in range(len(rotated)):
            for col in range(len(rotated[0])):
                mat[col][row] = rotated[row][col]

        for row in mat:
            row.reverse()
        
        if mat == target:
            return True
            
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                rotated[col][row] = mat[row][col]

        for row in rotated:
            row.reverse()
        
        if target == rotated:
            return True


        return False