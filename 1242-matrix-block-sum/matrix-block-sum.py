class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        answer = [[0] * len(mat[0]) for _ in range((len(mat)))]
        
        for row in range(len(answer)):
            for col in range(len(answer[0])):
                total = 0
                row_range = [max(0, row - k), min(row + k, len(answer) - 1)]
                col_range = [max(0, col - k), min(col + k, len(answer[0]) - 1)]

                for i in range(row_range[0], row_range[1] + 1):
                    for j in range(col_range[0], col_range[1] + 1):
                        total += mat[i][j]

                print(total)
                answer[row][col] = total 
        
        
        return answer
    