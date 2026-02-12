class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        top = [0, row - 1]
        bottom = [0, col - 1]

        output = []

        while top[0] <= top[1] and bottom[0] <= bottom[1]:
            temp = bottom[0] 
            for i in range(temp, bottom[1] + 1):
                output.append(matrix[top[0]][i])
            
            top[0] += 1

            if top[0] > top[1] or bottom[0] > bottom[1]:
                break
            
            temp = top[0]
            for i in range(temp, top[1] + 1):
                output.append(matrix[i][bottom[1]])

            bottom[1] -= 1
            
            if top[0] > top[1] or bottom[0] > bottom[1]:
                break
            
            temp = bottom[1]
            for i in range(temp, bottom[0] - 1, -1):
                output.append(matrix[top[1]][i])

            top[1] -= 1

            if top[0] > top[1] or bottom[0] > bottom[1]:
                break
            
            temp = top[1]
            for i in range(temp, top[0] - 1, -1):
                output.append(matrix[i][bottom[0]])

            bottom[0] += 1

        return output
