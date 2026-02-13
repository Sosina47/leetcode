class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = [mat[0][0]]
        row = len(mat)
        col = len(mat[0])

        x = y = 0
        for i in range(1, row + col - 1):
            if i % 2:
                y += 1

                while y >= col:
                    y -= 1
                    x += 1
                    
                while x < row and y < col:        
                    output.append(mat[x][y])
                    if x < row and y > 0:
                        y -= 1
                        x += 1
                    else:
                        break        

            else:
                x += 1
                while x >= row:
                    x -= 1
                    y += 1

                while x < row and y < col:
                    output.append(mat[x][y])

                    if x > 0 and y < col:
                        x -= 1
                        y += 1
                    else:
                        break

        return output
